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


text_numbers = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
}


def rename_numbers(line: str) -> str:
    while True:
        leftmost = {}
        for digit, txt in text_numbers.items():
            try:
                leftmost[digit] = line.index(txt)
            except ValueError:
                pass
        if not leftmost:
            return line
        leftmost = {k: v for k, v in sorted(leftmost.items(), key=lambda item: item[1])}
        digit = next(iter(leftmost))
        txt = text_numbers[digit]
        line = line.replace(txt, digit)



def parse_lines(lines):
    for line in lines:
        yield get_calibration_value(rename_numbers(line))


def load_file(filename):
    with open(filename, 'r') as f:
        yield from f.readlines()


def main():
    value = compute_value_from_file('input.txt')
    print(value)


def compute_value_from_file(filename):
    lines = load_file(filename)
    value = sum(parse_lines(lines))
    return value


if __name__ == '__main__':
    main()
