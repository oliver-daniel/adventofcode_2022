from dataclasses import dataclass
import itertools as it


N = [line.strip() for line in open('./in/14.txt').readlines()]
# N = [line.strip() for line in open('./in/14.test.txt').readlines()]


def smart_range(start, stop):
    if stop < start:
        return smart_range(stop, start)
    return range(start, stop + 1)


def make_blocked():
    blocked = set()
    for ln in N:
        chain = [(int(a), int(b)) for a, b in (x.split(',')
                                               for x in ln.split(' -> '))]
        for (jx, jy), (kx, ky) in it.pairwise(chain):
            for x, y in it.product(smart_range(jx, kx), smart_range(jy, ky)):
                blocked.add((x, y))

    return blocked


@dataclass
class Sand:
    x: int = 500
    y: int = 0

    def tup(self):
        return self.x, self.y


def part_1():
    blocked = make_blocked()
    at_rest = set()

    bottom = max(y for x, y in blocked)

    while True:
        sand = Sand()
        for height in range(bottom + 1):
            if (sand.x, height) not in blocked:
                sand.y = height
            elif (sand.x - 1, height) not in blocked:
                sand.y = height
                sand.x -= 1
            elif (sand.x + 1, height) not in blocked:
                sand.y = height
                sand.x += 1
            else:
                blocked.add(sand.tup())
                at_rest.add(sand.tup())
                break
        else:
            return len(at_rest)


def part_2():
    blocked = make_blocked()
    at_rest = set()

    bottom = 2 + max(y for x, y in blocked)

    while (500, 0) not in blocked:
        sand = Sand()
        for height in range(bottom):
            if (sand.x, height) not in blocked:
                sand.y = height
            elif (sand.x - 1, height) not in blocked:
                sand.y = height
                sand.x -= 1
            elif (sand.x + 1, height) not in blocked:
                sand.y = height
                sand.x += 1
            else:
                break
        # if we got here, we either broke early (i.e., got blocked)
        # or are on the floor
        blocked.add(sand.tup())
        at_rest.add(sand.tup())
    return len(at_rest)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())
