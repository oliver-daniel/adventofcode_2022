N = [line.strip() for line in open('./in/3.txt').readlines()]
# N = [line.strip() for line in open('./in/3.test.txt').readlines()]
from string import ascii_lowercase, ascii_uppercase

priorities = ascii_lowercase + ascii_uppercase


def part_1():
    t = 0
    for sack in N:
        L = len(sack) // 2
        common = (set(sack[:L]) & set(sack[L:])).pop()
        t += priorities.index(common) + 1
        
    return t

def part_2():
    t=0
    for a, b, c in zip(N[::3], N[1::3], N[2::3]):
        common = (set(a) & set(b) & set(c)).pop()
        t += priorities.index(common) + 1
    return t

if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())

