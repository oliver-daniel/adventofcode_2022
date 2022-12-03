N = [line.strip() for line in open('./in/2.txt').readlines()]
# N = [line.strip() for line in open('./in/2.test.txt').readlines()]

def _diff(a, b):
    if a + b in [
        'AY',
        'BZ',
        'CX'
    ]: return 1
    elif 'ABC'.index(a) == 'XYZ'.index(b): return 0
    else: return -1


def part_1():
    t = 0
    for a, b in map(str.split, N):
        t += 'XYZ'.index(b) + 1
        diff = _diff(a, b)
        if diff == 1: t += 6
        elif diff == 0: t += 3
    return t


def part_2():
    t = 0
    for a, b in map(str.split, N):
        opp_idx = 'ABC'.index(a)
        winning_idx = (opp_idx + 1) % 3
        losing_idx = 2 if opp_idx == 0 else opp_idx - 1

        # print(a, opp_idx, winning_idx)

        if b == 'X':
            t += losing_idx + 1
            # print(f'{losing_idx + 1} + 0')
        elif b == 'Y':
            t += 3 + opp_idx + 1
            # print(f'{opp_idx + 1} + 3')
        else:
            t += 6 + winning_idx + 1
            # print(f'{winning_idx + 1} + 7')
    return t

# X loses to B
# Y loses to C
# Z loses to A

if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())

