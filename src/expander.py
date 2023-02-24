from typing import Iterator

def expanded_form(num: int) -> str:
    return " + ".join(_expanded_form(num))

def _expanded_form(num: int) -> Iterator[str]:
    digits = str(num)
    parts = []
    for magnitude, digit in enumerate(reversed(digits), start=1):
        if digit != "0":
            parts.append(digit.ljust(magnitude, '0'))
        # zeros = '0' * magnitude
        # if digit != "0":
            # parts.append(f"{digit}{zeros}")
    return reversed(parts)
