from functools import cache
import itertools as it
from tqdm import tqdm
N = [line.strip() for line in open('./in/16.txt').readlines()]
# N = [line.strip() for line in open('./in/16.test.txt').readlines()]

L = len(N)

tunnels = {}
flow_rates = {}

for row in N:
    a, b = map(str.split, row.split('; '))
    valve = a[1]
    rate = int(a[-1][5:])
    tuns = [x.strip(',') for x in b[4:]]

    flow_rates[valve] = rate
    tunnels[valve] = tuns


worth_opening = {valve for valve, rate in flow_rates.items() if rate > 0}

dist = {v: {} for v in tunnels}

# precompute distances w Floyd-Warshall algorithm
# todo: optimize for non-worth valves


def _(u, v):
    return dist[u].get(v, float('inf'))


print("Precomputing...")
for valve, tuns in tunnels.items():
    for v in tuns:
        dist[valve][v] = 1
    dist[valve][valve] = 0
    for k, i, j in it.product(tunnels, repeat=3):
        dist[i][j] = min(_(i, j), _(i, k) + _(k, j))
        # dist[i][j] = max(dist[i].get(j, float('inf')), dist[i][k] + dist[k][j])


def part_1():
    def moves(t, location='AA', valves_open=set()):
        if t <= 0 or valves_open >= worth_opening:
            return 0

        expected_pressure = flow_rates[location] * (t - 1)
        spent_here = int(expected_pressure != 0)

        valves_open.add(location)

        return expected_pressure + max((moves(
            t - (spent_here + dist[location][v]),
            v,
            valves_open | {location}
        ) for v in worth_opening - valves_open), default=0)

    return moves(30)


def part_2():
    return "SLOW - 2602"
    def moves(t, valves_assigned, location='AA', valves_open=set()):
        if t <= 0 or valves_open >= valves_assigned:
            return 0

        expected_pressure = flow_rates[location] * (t - 1)
        spent_here = int(expected_pressure != 0)

        valves_open.add(location)

        return expected_pressure + max((moves(
            t - (spent_here + dist[location][v]),
            valves_assigned,
            v,
            valves_open | {location}
        ) for v in valves_assigned - valves_open), default=0)

    best = 0

    for k in tqdm(range(L // 2, 0, -1)):
        for elephant_assignments in map(set, it.combinations(worth_opening, k)):
            best = max(best, moves(26, elephant_assignments) +
                       moves(26, worth_opening - elephant_assignments))
        print(best)
    return best


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())
