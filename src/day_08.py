from collections import Counter

from src.timer import Timer

UNIQUE_LENGTHS = {
    2: "1",
    3: "7",
    4: "4",
    7: "8"
}


def countUniqueOutputs(input_file):
    unique_count = 0
    with open(input_file) as file:
        for line in file:
            output_combinations = line.split('|')[1].split()
            for combination in output_combinations:
                if len(combination) in UNIQUE_LENGTHS:
                    unique_count += 1
    return unique_count


def sortString(input_string):
    return ''.join(sorted(input_string))


def commonCount(l_string, r_string):
    common_letters = Counter(l_string) & Counter(r_string)
    return sum(common_letters.values())


def decodeOutput(entry):
    known_patterns = {}
    input_string, output_string = entry.split('|')
    input_combinations = input_string.split()
    remaining_inputs = []
    for combination in input_combinations:
        length = len(combination)
        sorted_combination = sortString(combination)
        if length in UNIQUE_LENGTHS:
            known_patterns[sorted_combination] = UNIQUE_LENGTHS[length]
            known_patterns[UNIQUE_LENGTHS[length]] = sorted_combination
        else:
            remaining_inputs.append(sortString(combination))

    for combination in remaining_inputs:
        length = len(combination)
        if length == 5:
            if commonCount(combination, known_patterns["1"]) == 2:
                known_patterns[combination] = "3"
            elif commonCount(combination, known_patterns["4"]) == 3:
                known_patterns[combination] = "5"
            else:
                known_patterns[combination] = "2"
        elif length == 6:
            if commonCount(combination, known_patterns["4"]) == 4:
                known_patterns[combination] = "9"
            elif commonCount(combination, known_patterns["1"]) == 2:
                known_patterns[combination] = "0"
            else:
                known_patterns[combination] = "6"

    result = ''
    for combination in output_string.split():
        result += known_patterns[sortString(combination)]

    return int(result)


def sumDecodedOutput(input_file):
    total_output = 0
    with open(input_file) as file:
        for line in file:
            total_output += decodeOutput(line)
    return total_output


if __name__ == '__main__':
    with Timer("Part 1"):
        part1_result = countUniqueOutputs("../input/day_08.txt")
    print(f"Part 1 Result: {part1_result}")
    with Timer("Part 2"):
        part2_result = sumDecodedOutput("../input/day_08.txt")
    print(f"Part 2 Result: {part2_result}")
