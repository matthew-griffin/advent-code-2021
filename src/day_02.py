from functools import partial


def incrementList(input_list, index, sign, value):
    input_list[index] += value if sign else -value


def calcPositionProduct(input_file):
    position = [0, 0]
    functions = {
        "forward": partial(incrementList, position, 0, True),
        "down": partial(incrementList, position, 1, True),
        "up": partial(incrementList, position, 1, False)
    }
    with open(input_file) as file:
        for line in file:
            parts = line.split()
            functions[parts[0]](int(parts[1]))

    return position[0] * position[1]


def calcCourseProduct(input_file):
    position = [0, 0]
    aim = 0

    with open(input_file) as file:
        for line in file:
            parts = line.split()
            command = parts[0]
            value = int(parts[1])
            if command == "up":
                aim -= value
            elif command == "down":
                aim += value
            elif command == "forward":
                position[0] += value
                position[1] += value * aim

    return position[0] * position[1]


if __name__ == '__main__':
    position_product = calcPositionProduct("../input/day_02.txt")
    print(f"Position Product: {position_product}")
    course_product = calcCourseProduct("../input/day_02.txt")
    print(f"Course Product: {course_product}")
