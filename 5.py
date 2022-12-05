data = open('./in/5.txt').read()
# data = open('./in/5.test.txt').read()

init, instructions = data.split('\n\n')
*init, L = init.splitlines()
instructions = instructions.splitlines()

L = int(L.split()[-1])


def make_stacks():
    stacks = [[] for _ in range(L)]
    for row in reversed(init):
        tokens = [row[i:i+1] for i in range(1, len(row), 4)]
        for i, tkn in enumerate(tokens):
            if tkn != ' ':
                stacks[i].append(tkn)
    return stacks


def part_1():
    stacks = make_stacks()

    for _, amt, _, origin, _, dest in map(str.split, instructions):
        amt = int(amt)
        origin = int(origin) - 1
        dest = int(dest) - 1

        for _ in range(amt):
            stacks[dest].append(stacks[origin].pop())

    return ("".join(stack[-1] for stack in stacks))


def part_2():
    stacks = make_stacks()

    for _, amt, _, origin, _, dest in map(str.split, instructions):
        amt = int(amt)
        origin = int(origin) - 1
        dest = int(dest) - 1

        stacks[dest].extend(stacks[origin][-amt:])
        del stacks[origin][-amt:]

    return ("".join(stack[-1] for stack in stacks))


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())
