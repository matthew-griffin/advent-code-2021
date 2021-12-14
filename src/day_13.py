import re

from src.timer import Timer


def getPointsAndFolds(input_file):
    points = set()
    folds = []
    with open(input_file) as file:
        line = file.readline().strip()
        while line:
            points.add(tuple([int(x) for x in line.split(',')]))
            line = file.readline().strip()
        line = file.readline().strip()
        while line:
            match = re.match(r'fold along (\w)=(\d+)', line)
            if match:
                folds.append((0 if match[1] == 'x' else 1, int(match[2])))
            line = file.readline().strip()

    return points, folds


def foldPoints(points, axis, index):
    out_points = set()
    for point in points:
        fold_value = point[axis]
        if fold_value > index:
            folded_value = index - (fold_value - index)
            x = point[0] if axis == 1 else folded_value
            y = point[1] if axis == 0 else folded_value
            out_points.add((x, y))
        else:
            out_points.add(point)
    return out_points


def calcDotsAfterFirstFold(input_file):
    points, folds = getPointsAndFolds(input_file)

    points = foldPoints(points, folds[0][0], folds[0][1])

    return len(points)


def getFoldedOutput(input_file):
    points, folds = getPointsAndFolds(input_file)
    for fold in folds:
        points = foldPoints(points, fold[0], fold[1])
    max_x = 0
    max_y = 0
    for x, y in points:
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    point_grid = [['.']*(max_x+1) for i in range(max_y+1)]
    for x, y in points:
        point_grid[y][x] = '#'
    result = ""
    for line in point_grid:
        result += "\n" + "".join(line)
    return result


if __name__ == '__main__':
    with Timer("Part 1"):
        part1_result = calcDotsAfterFirstFold("../input/day_13.txt")
    print(f"Part 1 Result: {part1_result}")
    with Timer("Part 2"):
        part2_result = getFoldedOutput("../input/day_13.txt")
    print(f"Part 2 Result: {part2_result}")
