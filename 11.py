import math
import operator
N = open('./in/11.txt').read().split('\n\n')
# N = open('./in/11.test.txt').read().split('\n\n')

conv = {
    '+': operator.add,
    '*': operator.mul,
}


class NaiveMonkey:
    def __init__(self, chunk):
        self.handled = 0
        _id, items, operation, test, true_dest, false_dest = map(
            str.strip, chunk.splitlines())
        self._id = int(_id.split()[1].strip(':'))

        self.items = [int(x.strip(',')) for x in items.split()[2:]]

        self.op, self.b = operation.split()[4:]
        op = conv[self.op]
        self.operation = lambda old: op(
            old,
            old if self.b == 'old' else int(self.b)
        )

        self.test = int(test.split()[-1])
        self.true_dest = int(true_dest.split()[-1])
        self.false_dest = int(false_dest.split()[-1])

    def act(self, monkeys):
        self.handled += len(self.items)
        for item in self.items:
            new = self.operation(item) // 3
            dest = [self.false_dest, self.true_dest][new % self.test == 0]
            monkeys[dest].items.append(new)
        self.items.clear()

    def __repr__(self):
        return f'<Monkey {self._id}: {self.items}, {self.true_dest} if |{self.test} else {self.false_dest}, inspected {self.handled}>'


class SmartMonkey(NaiveMonkey):
    def act(self, monkeys, all_mods):
        self.handled += len(self.items)
        for item in self.items:
            new = self.operation(item)
            dest = [self.false_dest, self.true_dest][new % self.test == 0]
            monkeys[dest].items.append(new % all_mods)
        self.items.clear()


def part_1():
    monkeys = [NaiveMonkey(chunk) for chunk in N]
    for _ in range(20):
        for monkey in monkeys:
            monkey.act(monkeys)
    activity = [monkey.handled for monkey in monkeys]
    activity.sort()
    return activity[-2] * activity[-1]


def part_2():
    monkeys = [SmartMonkey(chunk) for chunk in N]
    all_mods = math.lcm(*[
        monkey.test for monkey in monkeys
    ])

    for _ in range(10_000):
        for monkey in monkeys:
            monkey.act(monkeys, all_mods)

    activity = [monkey.handled for monkey in monkeys]
    activity.sort()
    return activity[-2] * activity[-1]


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())
