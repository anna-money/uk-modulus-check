import pytest

from uk_modulus_check import ModMode, ModRule, Weights, WeightTable

RULE_WITHOUT_EXCEPTION = "010004 016715 MOD11 0 0 0 0 0 0 8 7 6 5 4 3 2 1"
RULE_WITH_EXCEPTION = "070116 070116 MOD11 0 0 7 6 5 8 9 4 5 6 7 8 9 -1 12"


@pytest.mark.parametrize(
    "lines",
    [
        [RULE_WITHOUT_EXCEPTION],
        [RULE_WITH_EXCEPTION],
        [RULE_WITHOUT_EXCEPTION, RULE_WITH_EXCEPTION],
    ],
)
def test_reload(lines: list[str]) -> None:
    table = WeightTable()

    table.reload(lines)

    assert table.length() == len(lines)


@pytest.mark.parametrize("line", ["12", "a a a a a a a a a a a a a a a a a"])
def test_reload_invalid(line: str) -> None:
    table = WeightTable()

    with pytest.raises(ValueError):
        table.reload([line])


@pytest.mark.parametrize(
    ("sort_code", "expected"),
    [
        (
            70116,
            [
                ModRule(
                    start_code=70116,
                    end_code=70116,
                    mod_mode=ModMode.Mod11,
                    weights=Weights(u=0, v=0, w=7, x=6, y=5, z=8, a=9, b=4, c=5, d=6, e=7, f=8, g=9, h=-1),
                    exception=12,
                )
            ],
        ),
        (70117, []),
    ],
)
def test_try_get_rules(sort_code: int, expected: list[ModRule]) -> None:
    table = WeightTable()
    table.reload([RULE_WITH_EXCEPTION])

    assert table.try_get_rules(sort_code) == expected
