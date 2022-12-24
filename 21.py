from math import log10
import operator
import itertools
N = [line.strip() for line in open('./in/21.txt').readlines()]
# N = [line.strip() for line in open('./in/21.test.txt').readlines()]

monkeys = {}

for tokens in map(str.split, N):
    match tokens:
        case [monkey, num]:
            monkey = monkey.strip(':')
            monkeys[monkey] = int(num)
        case [monkey, a, op, b]:
            monkey = monkey.strip(':')
            monkeys[monkey] = (a, op, b)

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
}


def part_1():
    def evaluate(monkey):
        match monkeys[monkey]:
            case (a, op, b):
                return ops[op](evaluate(a), evaluate(b))
            case n:
                return n
    return evaluate('root')

def part_2():
    pass

def part_2_brute_force():
    _monkeys = monkeys.copy()
    def evaluate(monkey):
        match _monkeys[monkey]:
            case (a, op, b):
                return ops[op](evaluate(a), evaluate(b))
            case n:
                return n

    b = 83397964201949
    assert evaluate(_monkeys['root'][2]) == b
    result = 3451534022348
    _monkeys['humn'] = result
    assert evaluate(_monkeys['root'][0]) == b
    return result

if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())
