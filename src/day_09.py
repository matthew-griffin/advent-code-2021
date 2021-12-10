from functools import reduce

from src.timer import Timer


def populateGrid(input_file):
    grid = []
    with open(input_file) as file:
        for line in file:
            grid.append([int(char) for char in line if char.isdigit()])
    return grid


def findLowPoints(grid):
    height = len(grid)
    width = len(grid[0])
    low_points = {}
    for y in range(height):
        for x in range(width):
            curr_height = grid[y][x]
            if y > 0 and curr_height >= grid[y-1][x]:
                continue
            if x > 0 and curr_height >= grid[y][x-1]:
                continue
            if y < height - 1 and curr_height >= grid[y+1][x]:
                continue
            if x < width - 1 and curr_height >= grid[y][x+1]:
                continue
            low_points[(x, y)] = curr_height
    return low_points


def calcBasinArea(grid, x, y):
    if grid[y][x] >= 9:
        return 0

    grid[y][x] = 9
    height = len(grid)
    width = len(grid[0])
    points = 1
    if y > 0:
        points += calcBasinArea(grid, x, y-1)
    if x > 0:
        points += calcBasinArea(grid, x-1, y)
    if y < height - 1:
        points += calcBasinArea(grid, x, y+1)
    if x < width - 1:
        points += calcBasinArea(grid, x+1, y)
    return points


def sumRiskLevels(input_file):
    grid = populateGrid(input_file)
    low_points = findLowPoints(grid)

    return sum(low_points.values()) + len(low_points)


def calcBasinAreaProduct(input_file):
    grid = populateGrid(input_file)
    low_points = findLowPoints(grid)
    areas = []
    for point in low_points:
        areas.append(calcBasinArea(grid, point[0], point[1]))
    return reduce(lambda a, b: a * b, sorted(areas)[-3:])


if __name__ == '__main__':
    with Timer("Part 1"):
        part1_result = sumRiskLevels("../input/day_09.txt")
    print(f"Part 1 Result: {part1_result}")
    with Timer("Part 2"):
        part2_result = calcBasinAreaProduct("../input/day_09.txt")
    print(f"Part 2 Result: {part2_result}")
