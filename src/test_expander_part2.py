import pytest

import expander_part2 as expander


@pytest.mark.parametrize(
    "num, expected",
    (
        (1, "1"),
        (10, "10"),
        (11, "10 + 1"),
        (101, "100 + 1"),
        (70304, "70000 + 300 + 4"),
        (0, ""),
        (
            111111111111111111111,
            (
                "100000000000000000000 + 10000000000000000000 + 1000000000000000000 + "
                "100000000000000000 + 10000000000000000 + 1000000000000000 + "
                "100000000000000 + 10000000000000 + 1000000000000 + "
                "100000000000 + 10000000000 + 1000000000 + "
                "100000000 + 10000000 + 1000000 + "
                "100000 + 10000 + 1000 + 100 + 10 + 1"
            ),
        ),
    ),
)
def test_expanded_form(num, expected):
    assert expander.expanded_form(num) == expected


@pytest.mark.parametrize(
    "num, expected",
    (
        (0.1, "1/10"),
        (1.2, "1 + 2/10"),
        (0.12, "1/10 + 2/100"),
        (1.24, "1 + 2/10 + 4/100"),
        (0.04, "4/100"),
        (0.004, "4/1000"),
        (807.304, "800 + 7 + 3/10 + 4/1000"),
        (7.0004, "7 + 4/10000"),
        # test cases from hypothesis to check out:
        # 4078675579893530.0
        # -1.5
        # 1e-05
        # 3.923726177161579e+16
        # -4.46910601648927e+16
        # -inf
        # -nan
    ),
)
def test_expanded_form_part2(num, expected):
    assert expander.expanded_form(num) == expected
