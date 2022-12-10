N = [line.strip() for line in open('./in/10.txt').readlines()]
# N = [line.strip() for line in open('./in/10.test.txt').readlines()]
import itertools as it

cmds = [int(cmd.split()[1]) if cmd.startswith('addx') else cmd for cmd in N]

interesting = {20, 60, 100, 140, 180, 220}


def cycle():
    x = 1
    cycle = 1
    for cmd in it.cycle(cmds):
        if isinstance(cmd, int):
            yield cycle, x
            yield cycle + 1, x
            x += cmd
            cycle += 2
        else:
            yield cycle, x
            cycle += 1

def part_1():
    t = 0
    for cyc, x in cycle():
        if cyc in interesting:
            t += cyc * x
        
        if cyc > 220: return t


def part_2():
    screen = [0 for _ in range(6 * 40)]

    for cyc, x in cycle():
        col = (cyc - 1) % 40
        screen[cyc - 1] = x in [col - 1, col, col + 1]

        if cyc % 240 == 239: break
    
    for row in range(0, 240, 40):
        print("".join(' #'[px] for px in screen[row:row + 40]))
    return ""


if __name__ == '__main__':
    import sys
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())

