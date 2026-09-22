import pytest

from uk_modulus_check import SortCodeSubstitutionTable


@pytest.mark.parametrize("lines", [["1 2", "3 4"], ["1 2", "3 4", "5 6"]])
def test_reload(lines: list[str]) -> None:
    table = SortCodeSubstitutionTable()

    table.reload(lines)

    assert table.length() == len(lines)


def test_reload_invalid() -> None:
    table = SortCodeSubstitutionTable()

    with pytest.raises(ValueError):
        table.reload(["12"])


@pytest.mark.parametrize(("sort_code", "expected"), [(1, 2), (3, 4), (5, None)])
def test_try_get_substitution(sort_code: int, expected: int | None) -> None:
    table = SortCodeSubstitutionTable()
    table.reload(["1 2", "3 4"])

    assert table.try_get_substitution(sort_code) == expected
