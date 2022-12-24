import itertools as it
from collections import Counter
N = [line.strip() for line in open('./in/23.txt').readlines()]
# N = [line.strip() for line in open('./in/23.test.txt').readlines()]
# N = [line.strip() for line in open('./in/23.test.mini.txt').readlines()]
H = len(N)
W = len(N[0])

elves = {(i, j) for i, j in it.product(range(H), range(W)) if N[i][j] == "#"}


DEBUG = 0
if not DEBUG:
    debug = lambda *args, **kwargs: None
else:
    debug = print


def propose(G, elf, i):
    r, c = elf

    neighbours = (
        (r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
        (r, c - 1),                 (r, c + 1),
        (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)
    )

    if not any(spot in G for spot in neighbours):
        debug(elf, 'has no neighbours')
        return elf

    northbound = (
        (r - 1, c - 1), (r - 1, c), (r - 1, c + 1)
    )

    southbound = (
        (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)
    )

    westbound = (
        (r, c - 1), (r - 1, c - 1), (r + 1, c - 1)
    )

    eastbound = (
        (r, c + 1), (r - 1, c + 1), (r + 1, c + 1)
    )

    dirns = [
        (northbound, (r - 1, c)),
        (southbound, (r + 1, c)),
        (westbound, (r, c - 1)),
        (eastbound, (r, c + 1))
    ]

    for offset in range(4):
        dirn, proposal = dirns[(i + offset) % 4]
        if not any(spot in G for spot in dirn):
            return proposal
    else:
        debug('no directions work for', elf)
        return elf


def transition(curr, i):
    proposed_transition = {elf: propose(curr, elf, i) for elf in curr}
    ctr = Counter(proposed_transition.values())
    ret = {}
    for elf, proposal in proposed_transition.items():
        if ctr[proposal] > 1:
            debug(f"Can't move {elf} to {proposal}", ctr[proposal])
            ret[elf] = elf
        else:
            ret[elf] = proposal

    return ret


def part_1():
    curr = elves.copy()
    for i in range(10):
        curr = set(transition(curr, i).values())

    rs = [r for r, c in curr]
    cs = [c for r, c in curr]

    bounding_box = (max(rs) - min(rs) + 1) * (max(cs) - min(cs) + 1)
    return bounding_box - len(elves)


def part_2():
    curr = elves.copy()
    for i in it.count():
        new = transition(curr, i)
        if all(k == v for k, v in new.items()):
            return i + 1
        curr = set(new.values())


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())
