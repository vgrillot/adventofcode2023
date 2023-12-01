# https://adventofcode.com/2023/day/1

# https://adventofcode.com/2023/day/1/input


numbers = '0123456789'


def get_calibration_value(line: str) -> int:
    for a in line:
        if a in numbers:
            break
    else:
        a = '0'

    for b in line[::-1]:
        if b in numbers:
            break
    else:
        b = '0'

    return int(a + b)


def parse_lines(lines):
    for line in lines:
        yield get_calibration_value(line)


def load_file(filename):
    with open(filename, 'r') as f:
        yield from f.readlines()


def main():
    lines = load_file('input.txt')
    value = sum(parse_lines(lines))
    print(value)


if __name__ == '__main__':
    main()
