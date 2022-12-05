N = [line.strip() for line in open('./in/4.txt').readlines()]
# N = [line.strip() for line in open('./in/4.test.txt').readlines()]

def part_1():
    t = 0
    for row in N:
        (a, b), (c, d) = [map(int, x.split('-')) for x in row.split(',')]
        if a <= c <= d <= b or \
            c <= a <= b <= d:
            # print(a, b, c, d)
            t += 1
    return t

def part_2():
    t = 0
    for row in N:
        (a, b), (c, d) = [map(int, x.split('-')) for x in row.split(',')]
        # if set(range(a, b + 1)) & set(range(c, d + 1)):
        if a <= d and b >= c: # from https://stackoverflow.com/a/36035377
            t += 1
    return t

if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())

