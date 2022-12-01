N = [line.strip() for line in open('./in/1.txt').readlines()]
# N = [line.strip() for line in open('./in/1.test.txt').readlines()]

def part_1():
    elves = []
    t = 0
    for line in N:
        if not line:
            elves.append(t)
            t = 0
            continue
        t += int(line)
    elves.append(t)
    return max(elves)
    

def part_2():
    elves = []
    t = 0
    for line in N:
        if not line:
            elves.append(t)
            t = 0
            continue
        t += int(line)
    elves.append(t)
    elves.sort()
    return (sum(elves[-3:]))

if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())

