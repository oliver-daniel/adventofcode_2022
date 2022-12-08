import itertools as it
N = [[int(c) for c in line.strip()] for line in open('./in/8.txt').readlines()]
# N = [[int(c) for c in line.strip()] for line in open('./in/8.test.txt').readlines()]

H = len(N)
W = len(N[0])


def is_visible(G, r, c):
    if r == 0 or c == 0:
        return True

    node = G[r][c]

    to_left = G[r][:c]
    if all(node > x for x in to_left):
        return True

    if c == W - 1:
        return True
    to_right = G[r][c + 1:]
    if all(node > x for x in to_right):
        return True

    rows_above = G[:r]
    if all(node > row[c] for row in rows_above):
        return True

    if r == H - 1:
        return True
    rows_below = G[r + 1:]
    if all(node > row[c] for row in rows_below):
        return True

    return False


def part_1():
    return sum(1 for r, c in it.product(range(H), range(W)) if is_visible(N, r, c))


def viewing_score(G, r, c):
    node = G[r][c]
    if r == 0 or c == 0 or \
            r == H - 1 or c == W - 1:
        return 0
    to_left = G[r][:c][::-1]
    to_right = G[r][c + 1:]
    above = [j[c] for j in G[:r]][::-1]
    below = [j[c] for j in G[r + 1:]]

    t = 1
    for x in (above, to_left, to_right, below):
        score = 0
        for tree in x:
            score += 1
            if tree >= node:
                break

        t *= score
    return t


def part_2():
    return max(viewing_score(N, r, c) for r, c in it.product(range(H), range(W)))


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())
