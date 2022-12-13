N = [line.strip() for line in open('./in/13.txt').readlines()]
# N = [line.strip() for line in open('./in/13.test.txt').readlines()]

pairs = [(eval(a), eval(b)) for a, b in zip(N[::3], N[1::3])]


def compare(a, b):
    match a, b:
        case int(), int():
            return b - a
        case list(), list():
            for i, j in zip(a, b):
                if (k := compare(i, j)) != 0:
                    return k
            return len(b) - len(a)
        case int(), list():
            return compare([a], b)
        case list(), int():
            return compare(a, [b])


def part_1():
    # one liner:
    # return sum(i for i, (a, b) in enumerate(pairs, start=1) if compare(a, b) > 0)
    t = 0
    for i, (a, b) in enumerate(pairs, start=1):
        if compare(a, b) > 0:
            t += i
    return t


def part_2():
    from functools import cmp_to_key
    flat = [eval(x) for x in N if x] + [[[2]], [[6]]]
    flat.sort(key=cmp_to_key(compare), reverse=True)

    return (flat.index([[2]]) + 1) * (flat.index([[6]]) + 1)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())
