# https://adventofcode.com/2023/day/1

# https://adventofcode.com/2023/day/1/input


numbers = '0123456789'


def get_calibration_value(line: str) -> int:
    for a in line:
        if a in numbers:
            break
    for b in line[::-1]:
        if b in numbers:
            break
    return int(a + b)
