from functools import lru_cache

from src.timer import Timer


@lru_cache(maxsize=None)
def recursiveCalcNumFish(timer, days):
    if timer >= days:
        return 1

    fish_count = 1
    while days > timer:
        days -= timer + 1
        timer = 6
        fish_count += recursiveCalcNumFish(8, days)

    return fish_count


def calcNumFish(input_file, days):
    fish_timers = []
    with open(input_file) as file:
        for line in file:
            fish_timers += [int(value) for value in line.split(',')]

    fish_count = 0
    for timer in fish_timers:
        fish_count += recursiveCalcNumFish(timer, days)

    return fish_count


if __name__ == '__main__':
    with Timer("Part 1"):
        part1_result = calcNumFish("../input/day_06.txt", 80)
    print(f"Part 1 Result: {part1_result}")
    print(str(recursiveCalcNumFish.cache_info()))
    with Timer("Part 2"):
        part2_result = calcNumFish("../input/day_06.txt", 256)
    print(f"Part 2 Result: {part2_result}")
    print(str(recursiveCalcNumFish.cache_info()))
