N = [line.strip() for line in open('./in/25.txt').readlines()]
# N = [line.strip() for line in open('./in/25.test.txt').readlines()]


def snafu_to_b10(s):
    t = 0

    if s is not str:
        s = str(s)

    for i, b in enumerate(s[::-1]):
        if b == '-':
            b = -1
        elif b == '=':
            b = -2
        else:
            b = int(b)

        t += b * 5 ** i

    return t


def b10_to_snafu(n):
    if n <= 0:
        return ""

    q = n % 5

    if q <= 2:
        return b10_to_snafu(n // 5) + str(q)
    elif q == 3:
        return b10_to_snafu(n // 5 + 1) + "="
    else:
        return b10_to_snafu(n // 5 + 1) + '-'


def part_1():
    t = sum(map(snafu_to_b10, N))

    return b10_to_snafu(t)


def part_2():
    return "No stars yet :("


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())
