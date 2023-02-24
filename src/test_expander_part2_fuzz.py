import expander_part2
import typing
from hypothesis import given, strategies as st


@given(num=st.one_of(st.floats(), st.integers()))
def test_fuzz_expanded_form(num: typing.Union[float, int]) -> None:
    expander_part2.expanded_form(num=num)
