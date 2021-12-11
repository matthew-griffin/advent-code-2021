from src.timer import Timer

ADJACENT = [
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1)
]


def populateGrid(input_file):
    grid = []
    with open(input_file) as file:
        for line in file:
            grid.append([int(value) for value in line.strip()])
    return grid


def recCountFlashes(grid, flashed, x, y):
    if flashed[y][x] or grid[y][x] < 10:
        return 0

    flash_count = 1
    flashed[y][x] = True
    for diff in ADJACENT:
        off_x = x + diff[0]
        off_y = y + diff[1]
        if 0 <= off_y < len(grid) and 0 <= off_x < len(grid[0]):
            grid[off_y][off_x] += 1
            flash_count += recCountFlashes(grid, flashed, off_x, off_y)
    return flash_count


def countFlashesSingleStep(grid):
    height = len(grid)
    width = len(grid[0])
    flash_count = 0
    flashed = []
    for y in range(height):
        grid[y] = [value + 1 for value in grid[y]]
        flashed.append([False] * width)

    for y in range(height):
        for x in range(width):
            flash_count += recCountFlashes(grid, flashed, x, y)

    for y in range(height):
        for x in range(width):
            if flashed[y][x]:
                grid[y][x] = 0

    return flash_count


def countFlashes(input_file):
    grid = populateGrid(input_file)

    flash_count = 0
    for step in range(100):
        flash_count += countFlashesSingleStep(grid)

    return flash_count


def findFirstFullFlash(input_file):
    grid = populateGrid(input_file)
    grid_size = len(grid) * len(grid[0])

    steps = 1
    while countFlashesSingleStep(grid) != grid_size:
        steps += 1

    return steps


if __name__ == '__main__':
    with Timer("Part 1"):
        part1_result = countFlashes("../input/day_11.txt")
    print(f"Part 1 Result: {part1_result}")
    with Timer("Part 2"):
        part2_result = findFirstFullFlash("../input/day_11.txt")
    print(f"Part 2 Result: {part2_result}")
