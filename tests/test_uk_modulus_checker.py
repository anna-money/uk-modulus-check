import dataclasses
import pathlib

from uk_modulus_check import SortCodeSubstitutionTable, UKModulusChecker, WeightTable


@dataclasses.dataclass(slots=True, frozen=True, kw_only=True)
class TestCase:
    sort_code: str
    account_number: str
    expected_result: bool


BASE_DIR = pathlib.Path(__file__).resolve().parent
WEIGHTS = BASE_DIR / "data" / "weights.txt"
SUBSTITUTIONS = BASE_DIR / "data" / "subs.txt"


def _read_file(path: pathlib.Path) -> list[str]:
    with open(path, "r") as file:
        return file.readlines()


def test_validate() -> None:
    test_cases = [
        TestCase(sort_code="89999", account_number="66374958", expected_result=True),
        TestCase(sort_code="107999", account_number="88837491", expected_result=True),
        TestCase(sort_code="202959", account_number="63748472", expected_result=True),
        TestCase(sort_code="871427", account_number="46238510", expected_result=True),
        TestCase(sort_code="872427", account_number="46238510", expected_result=True),
        TestCase(sort_code="871427", account_number="9123496", expected_result=True),
        TestCase(sort_code="871427", account_number="99123496", expected_result=True),
        TestCase(sort_code="820000", account_number="73688637", expected_result=True),
        TestCase(sort_code="827999", account_number="73988638", expected_result=True),
        TestCase(sort_code="827101", account_number="28748352", expected_result=True),
        TestCase(sort_code="134020", account_number="63849203", expected_result=True),
        TestCase(sort_code="118765", account_number="64371389", expected_result=True),
        TestCase(sort_code="200915", account_number="41011166", expected_result=True),
        TestCase(sort_code="938611", account_number="7806039", expected_result=True),
        TestCase(sort_code="938600", account_number="42368003", expected_result=True),
        TestCase(sort_code="938063", account_number="55065200", expected_result=True),
        TestCase(sort_code="772798", account_number="99345694", expected_result=True),
        TestCase(sort_code="86090", account_number="6774744", expected_result=True),
        TestCase(sort_code="309070", account_number="2355688", expected_result=True),
        TestCase(sort_code="309070", account_number="12345668", expected_result=True),
        TestCase(sort_code="309070", account_number="12345677", expected_result=True),
        TestCase(sort_code="309070", account_number="99345694", expected_result=True),
        TestCase(sort_code="938063", account_number="15764273", expected_result=False),
        TestCase(sort_code="938063", account_number="15764264", expected_result=False),
        TestCase(sort_code="938063", account_number="15763217", expected_result=False),
        TestCase(sort_code="118764", account_number="64371388", expected_result=False),
        TestCase(sort_code="203099", account_number="66831036", expected_result=False),
        TestCase(sort_code="203099", account_number="58716970", expected_result=False),
        TestCase(sort_code="89999", account_number="66374959", expected_result=False),
        TestCase(sort_code="107999", account_number="88837493", expected_result=False),
        TestCase(sort_code="74456", account_number="12345112", expected_result=True),
        TestCase(sort_code="70116", account_number="34012583", expected_result=True),
        TestCase(sort_code="74456", account_number="11104102", expected_result=True),
        TestCase(sort_code="180002", account_number="190", expected_result=True),
        # ANNA
        TestCase(sort_code="040344", account_number="00000023", expected_result=True),
        TestCase(sort_code="040344", account_number="000000120", expected_result=True),
    ]

    weight_table = WeightTable()
    weight_table.reload(_read_file(WEIGHTS))

    sort_code_substitution_table = SortCodeSubstitutionTable()
    sort_code_substitution_table.reload(_read_file(SUBSTITUTIONS))

    checker = UKModulusChecker(weight_table, sort_code_substitution_table)

    for case in test_cases:
        result = checker.validate(int(case.sort_code), int(case.account_number))
        if result.result != case.expected_result:
            print(
                f"FAIL: S/C {case.sort_code} A/N {case.account_number} expected {case.expected_result} got {result}"
            )
