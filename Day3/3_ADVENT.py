f = open("3_input.txt", "r")
lines = f.readlines()

algo_list = []
for line in lines:
	algo_list.append(line.rstrip().split(','))


def walk(line):
    x, y = 0, 0
    for step in line.split(','):
        c, n = step[0], int(step[1:])
        for _ in range(n):
            yield (x, y)
            if c == 'U':
                y += 1
            elif c == 'L':
                x -= 1
            elif c == 'D':
                y -= 1
            elif c == 'R':
                x += 1
    yield (x, y)


def part1(lines):
    result, field = None, {}
    for i, line in enumerate(lines):
        for x, y in walk(line):
            if (x or y) and field.setdefault((x, y), i) != i:
                manhattan = abs(x) + abs(y)
                if result is None or result > manhattan:
                    result = manhattan
    return result
	
def part2(lines):
    result, field, distances = None, {}, {}
    for i, line in enumerate(lines):
        distance = 0
        for x, y in walk(line):
            if not x and not y:
                pass
            elif (x, y) not in field:
                field[(x, y)] = i
                distances[(x, y)] = distance
            elif field[(x, y)] != i:
                other = distances[(x, y)]
                if result is None or result > other + distance:
                    result = other + distance
                if other > distance:
                    field[(x, y)] = i
                    distances[(x, y)] = distance
            distance += 1
    return result


print(part1(lines))
print(part2(lines))