N = [line.strip() for line in open('./in/6.txt').readlines()]
# N = [line.strip() for line in open('./in/6.test.txt').readlines()]

def part_1():
    for row in N:
        for i in range(4, len(row)):
            if len(set(row[i-4:i])) == 4:
                return i

def part_2():
    for row in N:
        for i in range(14, len(row)):
            if len(set(row[i-14:i])) == 14:
                return i

if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())

