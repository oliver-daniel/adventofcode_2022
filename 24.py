from functools import cache
import itertools as it
import heapq
from collections import defaultdict

N = [line.strip() for line in open('./in/24.txt').readlines()]
# N = [line.strip() for line in open('./in/24.test.txt').readlines()]
# N = [line.strip() for line in open('./in/24.test.mini.txt').readlines()]

# ignore #s on border
N = [row[1:-1] for row in N[1:-1]]

H = len(N)
W = len(N[0])

blizzard_locations = [
    ((i, j), N[i][j])
    for i, j in it.product(range(H), range(W))
    if N[i][j] != '.'
]

START = (-1, 0)
END = (H, W - 1)

debug = [
    lambda *args, **kwargs: None,
    print
][False]

# lists of tuples (r, q) such that if turn % q == r,
# then the tile is unavailable

mods = [[[] for _ in range(W)] for _ in range(H)]

for (row, col), dirn in blizzard_locations:
    if dirn in '<>':
        for offset in range(W):
            d = -offset if dirn == '<' else offset
            mods[row][(col + d) % W].append((offset, W))
    else:
        for offset in range(H):
            d = -offset if dirn == '^' else offset
            mods[(row + d) % H][col].append((offset, H))

def is_available(turn, i, j):
    if (i, j) in (START, END): return True
    try:
        cell = mods[i][j]
    except IndexError:
        print(i, j, H, W)
        raise
    return not any(
        turn % q == r for r, q in cell
    )

def neighbors(r, c):
    for dx in [-1, 1]:
        if 0 <= (j := r + dx) < H and 0 <= c < W:
            yield j, c
        if 0 <= (k := c + dx) < W and 0 <= r < H:
            yield r, k
        # also yield staying put
        yield r, c
        # special case: if it's the start or end
        if (j, c) in (START, END):
            yield (j, c)

@cache
def dijkstras(start_turn = 0, start = START, dest = END):
    # def h(j, k):
    #     j_end, k_end = END
    #     return abs(j - j_end) + abs(k - k_end)

    seen = set()

    shortest_path_to = defaultdict(lambda: float('inf'))
    shortest_path_to[start] = start_turn

    unvisited = [(start_turn, start)]

    while unvisited:
        turn, curr = heapq.heappop(unvisited)
        debug("\nAt", curr, "best so far is on turn", turn)

        for neighbor in neighbors(*curr):
            debug("Trying", neighbor)


            if is_available(turn + 1, *neighbor):
                debug("...which is available")

            d = turn + 1 if is_available(turn + 1, *neighbor) else float('inf')
            
            if d < shortest_path_to[neighbor]:
                shortest_path_to[neighbor] = d
            if d < float('inf'):
                tup = (turn + 1, neighbor, d)
                if tup not in seen:
                    heapq.heappush(unvisited, (turn + 1, neighbor))
                    seen.add(tup)
                else:
                    debug('skipping seen')
            if neighbor == dest and d < float('inf'):
                debug("Found the end!")
                return turn + 1
    
    # return shortest_path_to[END]
            



def part_1():
    return dijkstras(0)

def part_2():
    trip_1 = dijkstras(0)
    # print('trip one takes', trip_1)
    return_trip = dijkstras(trip_1, END, START)
    # print('trip two takes', return_trip)
    return dijkstras(return_trip)

if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())

