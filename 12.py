import itertools as it
from string import ascii_lowercase
import heapq
from collections import defaultdict
N = [line.strip() for line in open('./in/12.txt').readlines()]
# N = [line.strip() for line in open('./in/12.test.txt').readlines()]

H = len(N)
W = len(N[0])

START = 'S'
TARGET = 'E'

elev = {k: i for i, k in enumerate(ascii_lowercase)}
elev['S'] = 0
elev['E'] = 25


def neighbors(G, r, c):
    for dx in [-1, 1]:
        if 0 <= (j := r + dx) < H:
            yield j, c
        if 0 <= (k := c + dx) < W:
            yield r, k


def a_star(r, c, end):
    def h(j, k):
        return abs(j - end[0]) + abs(k - end[1])

    min_steps_to = {(r, c): 0}

    g_score = defaultdict(lambda: float('inf'))
    g_score[r, c] = 0

    f_score = defaultdict(lambda: float('inf'))
    f_score[r, c] = 0 + h(r, c)

    open_set = [(f_score[r, c], (r, c))]

    while len(open_set) > 0:
        cost, curr = heapq.heappop(open_set)
        node = N[curr[0]][curr[1]]
        if node == TARGET:
            return min_steps_to[curr]

        for j, k in neighbors(N, *curr):
            new_elev = elev[N[j][k]]
            curr_elev = elev[node]
            # why does this need to be 1?
            d = 1 if new_elev - curr_elev <= 1 else float('inf')
            score = g_score[curr] + d

            if score < g_score[j, k]:
                min_steps_to[j, k] = min_steps_to[curr] + 1
                g_score[j, k] = score
                f_score[j, k] = score + h(j, k)

                coords = [x for _, x in open_set]

                if (j, k) not in coords:
                    heapq.heappush(open_set, (f_score[j, k], (j, k)))
    return -1


def part_1():
    start = next((r, c) for r, c in it.product(
        range(H), range(W)) if N[r][c] == START)
    end = next((r, c) for r, c in it.product(
        range(H), range(W)) if N[r][c] == TARGET)

    return a_star(*start, end)


def part_2():
    best_so_far = float('inf')
    end = next((r, c) for r, c in it.product(
        range(H), range(W)) if N[r][c] == TARGET)
    for r, c in it.product(range(H), range(W)):
        if N[r][c] != 'a':
            continue
        if 0 < (k := a_star(r, c, end)) < best_so_far:
            best_so_far = k
    return best_so_far


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())
