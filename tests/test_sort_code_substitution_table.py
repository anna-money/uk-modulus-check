import pytest

from uk_modulus_check import SortCodeSubstitutionTable


def test_load() -> None:
    table = SortCodeSubstitutionTable()

    table.load(["1 2", "3 4"])
    assert table.length() == 2

    table.load(["1 2", "3 4", "5 6"])
    assert table.length() == 3

    with pytest.raises(ValueError):
        table.load(["12"])


def test_try_get_substitution() -> None:
    table = SortCodeSubstitutionTable()
    table.load(["1 2", "3 4"])

    assert table.try_get_substitution(1) == 2
    assert table.try_get_substitution(3) == 4
    assert not table.try_get_substitution(5)
