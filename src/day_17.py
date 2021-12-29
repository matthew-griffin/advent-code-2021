import re

from src.timer import Timer


def tryVelocity(x_vel, y_vel, target_area):
    x, y = 0, 0
    while x <= target_area[1] and y >= target_area[2]:
        if x >= target_area[0] and y <= target_area[3]:
            return True
        x += x_vel
        y += y_vel
        x_vel = x_vel - 1 if x_vel > 0 else 0
        y_vel -= 1
    return False


def getTargetArea(input_string):
    match = re.findall(r'target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)', input_string)
    return [int(i) for i in match[0]]


def findMaximumHeight(input_string):
    target_area = getTargetArea(input_string)
    min_y = target_area[2]
    return min_y * (min_y + 1) // 2


def countPossibleVelocities(input_string):
    target_area = getTargetArea(input_string)
    possible_velocities = 0

    for x_vel in range(target_area[1]+1):
        for y_vel in range(target_area[2]-1, -target_area[2]+1):
            if tryVelocity(x_vel, y_vel, target_area):
                possible_velocities += 1

    return possible_velocities


if __name__ == '__main__':
    input_string = "target area: x=70..125, y=-159..-121"
    with Timer("Part 1"):
        part1_result = findMaximumHeight(input_string)
    print(f"Part 1 Result: {part1_result}")
    with Timer("Part 2"):
        part2_result = countPossibleVelocities(input_string)
    print(f"Part 2 Result: {part2_result}")
