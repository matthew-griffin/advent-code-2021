from collections import Counter

from src.timer import Timer


def calcMinimumFuel1(input_file):
    with open(input_file) as file:
        crab_positions = Counter([int(value) for value in file.readline().split(',')])

    min_val = min(crab_positions)
    max_val = max(crab_positions)
    cheapest_cost = None

    for test_position in range(min_val, max_val+1):
        test_cost = 0
        for position, count in crab_positions.items():
            test_cost += abs(test_position-position) * count
        if cheapest_cost is None or test_cost <= cheapest_cost:
            cheapest_cost = test_cost

    return cheapest_cost


def triangularNumber(n):
    return n * (n + 1) // 2


def calcMinimumFuel2(input_file):
    with open(input_file) as file:
        crab_positions = Counter([int(value) for value in file.readline().split(',')])

    min_val = min(crab_positions)
    max_val = max(crab_positions)
    cheapest_cost = None

    for test_position in range(min_val, max_val+1):
        test_cost = 0
        for position, count in crab_positions.items():
            test_cost += triangularNumber(abs(test_position-position)) * count
        if cheapest_cost is None or test_cost <= cheapest_cost:
            cheapest_cost = test_cost

    return cheapest_cost


if __name__ == '__main__':
    with Timer("Part 1"):
        part1_result = calcMinimumFuel1("../input/day_07.txt")
    print(f"Part 1 Result: {part1_result}")
    with Timer("Part 2"):
        pass
        part2_result = calcMinimumFuel2("../input/day_07.txt")
    print(f"Part 2 Result: {part2_result}")
