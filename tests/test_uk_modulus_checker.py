import pathlib

import pytest

from uk_modulus_check import (
    SortCodeSubstitutionTable,
    UKModulusChecker,
    ValidationResult,
    WeightTable,
)

DATA_DIR = pathlib.Path(__file__).resolve().parent / "data"


@pytest.fixture(scope="module")
def checker() -> UKModulusChecker:
    weight_table = WeightTable()
    weight_table.reload((DATA_DIR / "weights.txt").read_text().splitlines())

    sort_code_substitution_table = SortCodeSubstitutionTable()
    sort_code_substitution_table.reload((DATA_DIR / "subs.txt").read_text().splitlines())

    return UKModulusChecker(weight_table, sort_code_substitution_table)


def _passed(*, substitute_sort_code: int | None = None) -> ValidationResult:
    return ValidationResult(result=True, known_sort_code=True, substitute_sort_code=substitute_sort_code)


def _failed() -> ValidationResult:
    return ValidationResult(result=False, known_sort_code=True, substitute_sort_code=None)


def _unknown_sort_code() -> ValidationResult:
    return ValidationResult(result=True, known_sort_code=False, substitute_sort_code=None)


@pytest.mark.parametrize(
    ("sort_code", "account_number", "expected"),
    [
        ("89999", "66374958", _passed()),
        ("107999", "88837491", _passed()),
        ("202959", "63748472", _passed()),
        ("871427", "46238510", _passed()),
        ("872427", "46238510", _passed()),
        ("871427", "9123496", _passed()),
        ("871427", "99123496", _passed()),
        ("820000", "73688637", _passed()),
        ("827999", "73988638", _passed()),
        ("827101", "28748352", _passed()),
        ("134020", "63849203", _passed()),
        ("118765", "64371389", _passed()),
        ("200915", "41011166", _passed()),
        ("938611", "7806039", _passed()),
        ("938600", "42368003", _passed()),
        ("938063", "55065200", _passed()),
        ("772798", "99345694", _passed()),
        ("86090", "6774744", _passed()),
        ("309070", "2355688", _passed()),
        # Exception 9: validated against the substitute sort code 309634.
        ("309070", "12345668", _passed(substitute_sort_code=309634)),
        ("309070", "12345677", _passed()),
        ("309070", "99345694", _passed()),
        ("938063", "15764273", _failed()),
        ("938063", "15764264", _failed()),
        ("938063", "15763217", _failed()),
        ("118764", "64371388", _failed()),
        ("203099", "66831036", _failed()),
        ("203099", "58716970", _failed()),
        ("89999", "66374959", _failed()),
        ("107999", "88837493", _failed()),
        ("74456", "12345112", _passed()),
        ("70116", "34012583", _passed()),
        ("74456", "11104102", _passed()),
        ("180002", "190", _passed()),
        # ANNA: 040344 is a MOD10 rule; 00000020 is a synthetic number that satisfies it.
        ("040344", "00000023", _failed()),
        ("040344", "000000120", _failed()),
        ("040344", "00000020", _passed()),
        ("231185", "00002221", _passed()),
        # 050095 was carved out of 050022-058999, so it has no rule and is not checked.
        ("050095", "12345678", _unknown_sort_code()),
    ],
)
def test_validate(
    checker: UKModulusChecker,
    sort_code: str,
    account_number: str,
    expected: ValidationResult,
) -> None:
    assert checker.validate(int(sort_code), int(account_number)) == expected
