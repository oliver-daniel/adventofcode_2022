from dataclasses import dataclass
import itertools as it
N = [line.strip() for line in open('./in/9.txt').readlines()]
# N = [line.strip() for line in open('./in/9.test.txt').readlines()]
# N = [line.strip() for line in open('./in/9.p2.test.txt').readlines()]


@dataclass
class Point:
    x: int
    y: int

    @property
    def tup(self):
        return (self.x, self.y)


def part_1():
    head = Point(0, 0)
    tail = Point(0, 0)

    visited = set()

    for dirn, dist in map(str.split, N):
        # print('===', dirn, dist, '===')
        dist = int(dist)
        for _ in range(dist):
            match dirn:
                case 'U': head.y += 1
                case 'R': head.x += 1
                case 'D': head.y -= 1
                case 'L': head.x -= 1
            # print('Head at', head.tup)
            # print('Tail currently at', tail.tup)
            dx = head.x - tail.x
            dy = head.y - tail.y
            if abs(dx) < 2 and abs(dy) < 2:
                # print('no move')
                # print()
                continue

            dx = dx // abs(dx or 1)
            dy = dy // abs(dy or 1)
            tail.x += dx
            tail.y += dy

            # print(f'Moved by {dx = } {dy = }')
            # print("New location:", tail.tup)
            # print()

            visited.add(tail.tup)

    return len(visited)


def part_2():
    chain = [Point(0, 0) for _ in range(10)]
    visited = set()

    for dirn, dist in map(str.split, N):
        dist = int(dist)
        for _ in range(dist):
            head = chain[0]
            match dirn:
                case 'U': head.y += 1
                case 'R': head.x += 1
                case 'D': head.y -= 1
                case 'L': head.x -= 1
            for lead, follow in zip(chain, chain[1:]):
                dx = lead.x - follow.x
                dy = lead.y - follow.y

                if abs(dx) < 2 and abs(dy) < 2:
                    continue

                dx = dx // abs(dx or 1)
                dy = dy // abs(dy or 1)
                follow.x += dx
                follow.y += dy
            visited.add(chain[-1].tup)
    return len(visited)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())
