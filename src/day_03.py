from src.timer import Timer


def calcPowerUsage(input_file):
    bit_width = None
    zero_count = None
    one_count = None

    with open(input_file) as file:
        for line in file:
            if bit_width is None:
                bit_width = len(line) - 1
                zero_count = [0] * bit_width
                one_count = [0] * bit_width
            for index in range(bit_width):
                if line[index] is '0':
                    zero_count[index] += 1
                else:
                    one_count[index] += 1

    gamma = ""
    epsilon = ""
    for zero, one in zip(zero_count, one_count):
        gamma += "1" if one > zero else "0"
        epsilon += "1" if one < zero else "0"

    return int(gamma, 2) * int(epsilon, 2)


def recursiveReduceValues(input_list, index, keep_greater):
    zero_strings = []
    one_strings = []

    for line in input_list:
        if line[index] is '0':
            zero_strings.append(line)
        elif line[index] is '1':
            one_strings.append(line)

    zero_count = len(zero_strings)
    one_count = len(one_strings)
    if zero_count == one_count and zero_count == 1:
        return one_strings[0] if keep_greater else zero_strings[0]

    if zero_count == 0 and one_count == 1:
        return one_strings[0]

    if zero_count == 1 and one_count == 0:
        return zero_strings[0]

    if bool(zero_count > one_count) != bool(not keep_greater):
        return recursiveReduceValues(zero_strings, index+1, keep_greater)
    else:
        return recursiveReduceValues(one_strings, index+1, keep_greater)


def calcLifeSupportRating(input_file):
    zero_strings = []
    one_strings = []

    with open(input_file) as file:
        for line in file:
            if line[0] is '0':
                zero_strings.append(line.strip())
            elif line[0] is '1':
                one_strings.append(line.strip())

    zero_count = len(zero_strings)
    one_count = len(one_strings)
    oxygen_strings = zero_strings if zero_count > one_count else one_strings
    co2_strings = zero_strings if zero_count < one_count else one_strings

    oxygen_rating = recursiveReduceValues(oxygen_strings, 1, True)
    co2_rating = recursiveReduceValues(co2_strings, 1, False)

    return int(oxygen_rating, 2) * int(co2_rating, 2)


if __name__ == '__main__':
    with Timer("Part 1"):
        part1_result = calcPowerUsage("../input/day_03.txt")
    print(f"Part 1 Result: {part1_result}")
    with Timer("Part 2"):
        part2_result = calcLifeSupportRating("../input/day_03.txt")
    print(f"Part 2 Result: {part2_result}")
