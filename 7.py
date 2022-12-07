from collections import defaultdict
N = [line.strip() for line in open('./in/7.txt').readlines()]
# N = [line.strip() for line in open('./in/7.test.txt').readlines()]


sizes = defaultdict(lambda: 0)
seek = 1
stack = ['']
while True:
    row = N[seek]
    if row.startswith('$'):
        match row.split()[1:]:
            case ['cd', '..']:
                stack.pop()
                seek += 1
            case ['cd', r]:
                stack.append(r)
                seek += 1
            case ['ls']:
                new_seek = seek + 1
                while new_seek < len(N):
                    k = N[new_seek]
                    if k.startswith('$'):
                        break
                    elif not k.startswith('dir'):
                        size = int(k.split()[0])
                        for ssq in range(len(stack)):
                            sizes['/'.join(stack[:ssq + 1])] += size
                        # sizes['/'.join(stack)] += size
                    new_seek += 1
                seek = new_seek
        # seek += 1
        if seek >= len(N):
            break


def part_1():
    t = 0
    for k, v in sizes.items():
        if v <= 100000:
            t += v
    return t


def part_2():
    unused = 70000000 - sizes['']
    would_be_enough = [
        v for k, v in sizes.items() if unused + v >= 30000000
    ]
    return min(would_be_enough)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())
