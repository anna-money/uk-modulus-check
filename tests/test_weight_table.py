import pytest

from uk_modulus_check import WeightTable


def test_load():
    table = WeightTable()

    table.load(["010004 016715 MOD11 0 0 0 0 0 0 8 7 6 5 4 3 2 1"])
    assert table.length() == 1

    table.load(["070116 070116 MOD11 0 0 7 6 5 8 9 4 5 6 7 8 9 -1 12"])
    assert table.length() == 1

    with pytest.raises(ValueError):
        table.load(["12"])

    with pytest.raises(ValueError):
        table.load(["a a a a a a a a a a a a a a a a a"])


def test_try_get_rules():
    sort_code = int("070116")

    table = WeightTable()
    table.load(["070116 070116 MOD11 0 0 7 6 5 8 9 4 5 6 7 8 9 -1 12"])

    actual = table.try_get_rules(sort_code)
    assert len(actual) == 1
    assert actual[0].start_code == sort_code
    assert actual[0].end_code == sort_code
