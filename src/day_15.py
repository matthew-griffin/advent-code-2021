import sys
from collections import defaultdict
from functools import lru_cache
from heapq import heappush, heappop

from src.timer import Timer

OFFSETS = (
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
)


def reconstruct_path(cameFrom, current):
    total_path = [current]
    while current in cameFrom:
        current = cameFrom[current]
        total_path.append(current)
    return total_path


# Shamelessly ripped from https://en.wikipedia.org/wiki/A*_search_algorithm
# A* finds a path from start to goal.
# h is the heuristic function. h(n) estimates the cost to reach goal from node n.
def A_Star(start, goal, h, d):
    # The set of discovered nodes that may need to be (re-)expanded.
    # Initially, only the start node is known.
    # This is usually implemented as a min-heap or priority queue rather than a hash-set.
    openSet = []
    heappush(openSet, (h(start), start))

    # For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from start
    # to n currently known.
    cameFrom = {}

    # For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
    gScore = defaultdict(lambda: sys.maxsize)
    gScore[start] = 0

    # For node n, fScore[n] := gScore[n] + h(n). fScore[n] represents our current best guess as to
    # how short a path from start to finish can be if it goes through n.
    fScore = defaultdict(lambda: sys.maxsize)
    fScore[start] = h(start)

    while len(openSet):
        # This operation can occur in O(1) time if openSet is a min-heap or a priority queue
        current = heappop(openSet)[1]
        if current == goal:
            return reconstruct_path(cameFrom, current)

        for offset in OFFSETS:
            neighbor = (current[0] + offset[0], current[1] + offset[1])
            if neighbor[0] < 0 or neighbor[1] < 0 or neighbor[0] > goal[0] or neighbor[1] > goal[1]:
                continue
            # d(current,neighbor) is the weight of the edge from current to neighbor
            # tentative_gScore is the distance from start to the neighbor through current
            tentative_gScore = gScore[current] + d(neighbor)
            if tentative_gScore < gScore[neighbor]:
                # This path to neighbor is better than any previous one. Record it!
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = tentative_gScore + h(neighbor)
                queue_tuple = (fScore[neighbor], neighbor)
                heappush(openSet, queue_tuple)

    # Open set is empty but goal was never reached
    raise RuntimeError("Goal never reached")


def populateGrid(input_file):
    grid = []
    with open(input_file) as file:
        for line in file:
            grid.append([int(char) for char in line if char.isdigit()])
    return grid, len(grid[0]), len(grid)


def calcLowestRisk(input_file):
    grid, width, height = populateGrid(input_file)

    path = A_Star((0, 0), (width - 1, height - 1),
                  lambda node: (width-node[0])+(height-node[1]),
                  lambda neighbour: grid[neighbour[1]][neighbour[0]])
    result = 0
    for point in path[0:-1]:
        result += grid[point[1]][point[0]]

    return result


def calcMultiGridCost(grid, width, height, point):
    x = point[0] % width
    y = point[1] % height
    base_cost = grid[y][x]
    x_block = point[0] // width
    y_block = point[1] // height
    cost = base_cost + x_block + y_block
    while cost > 9:
        cost -= 9

    return cost


def calcLowestRiskPart2(input_file):
    grid, width, height = populateGrid(input_file)

    @lru_cache(maxsize=None)
    def cachedMultiGridCost(point):
        return calcMultiGridCost(grid, width, height, point)

    full_width = width * 5
    full_height = width * 5

    path = A_Star((0, 0), (full_width - 1, full_height - 1),
                  lambda node: (full_width - node[0])+(full_height - node[1]),
                  cachedMultiGridCost)
    result = 0
    for path_point in path[0:-1]:
        result += cachedMultiGridCost(path_point)
    return result


if __name__ == '__main__':
    with Timer("Part 1"):
        part1_result = calcLowestRisk("../input/day_15.txt")
    print(f"Part 1 Result: {part1_result}")
    with Timer("Part 2"):
        part2_result = calcLowestRiskPart2("../input/day_15.txt")
    print(f"Part 2 Result: {part2_result}")
