import re

from src.timer import Timer


def createInclusiveRange(start, stop):
    if stop > start:
        return range(start, stop+1)
    return range(start, stop-1, -1)


def addPoint(point, point_counts):
    if point in point_counts:
        point_counts[point] += 1
    else:
        point_counts[point] = 1


def countOverlappingPoints(input_file, consider_diagonal):
    point_counts = {}
    with open(input_file) as file:
        for line in file:
            start_x, start_y, stop_x, stop_y = [int(s) for s in re.findall(r'\b\d+\b', line)]

            if start_x == stop_x:
                for y in createInclusiveRange(start_y, stop_y):
                    addPoint((start_x, y), point_counts)
            elif start_y == stop_y:
                for x in createInclusiveRange(start_x, stop_x):
                    addPoint((x, start_y), point_counts)
            elif consider_diagonal:
                for x, y in zip(createInclusiveRange(start_x, stop_x), createInclusiveRange(start_y, stop_y)):
                    addPoint((x, y), point_counts)

    return sum(value > 1 for value in point_counts.values())


if __name__ == '__main__':
    with Timer("Part 1"):
        part1_result = countOverlappingPoints("../input/day_05.txt", False)
    print(f"Part 1 Result: {part1_result}")
    with Timer("Part 2"):
        part2_result = countOverlappingPoints("../input/day_05.txt", True)
    print(f"Part 2 Result: {part2_result}")
