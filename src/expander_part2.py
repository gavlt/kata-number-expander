from typing import Iterator, NamedTuple

class Digits(NamedTuple):
    whole: str
    fractional: str = ""

def expanded_form(num: float|int) -> str:
    return " + ".join(_expanded_form(num))

def _expanded_form(num: float|int) -> Iterator[str]:
    digits = Digits(*str(num).split("."))
    yield from _expand_ints(digits.whole)
    yield from _expand_decimals(digits.fractional)

def _expand_ints(digits: str) -> Iterator[str]:
    parts = []
    for magnitude, digit in enumerate(reversed(digits), start=1):
        if digit != "0":
            parts.append(digit.ljust(magnitude, '0'))
    yield from reversed(parts)

def _expand_decimals(digits: str) -> Iterator[str]:
    for magnitude, digit in enumerate(digits, start=1):
        if digit != "0":
            yield f"{digit}/{10 ** magnitude}"
