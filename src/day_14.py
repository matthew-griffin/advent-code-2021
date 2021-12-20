from collections import Counter

from src.timer import Timer


def calcElementRange(input_file, steps):
    template = None
    expanded_rules = {}
    with open(input_file) as file:
        for line in file:
            if template is None:
                template = line.strip()
            elif len(line) > 1:
                pair, insertion = line.split("->")
                pair = pair.strip()
                insertion = insertion.strip()
                expanded_rules[pair] = (pair[0]+insertion, insertion+pair[1])

    pair_counts = Counter()
    for char in range(len(template) - 1):
        pair_counts[template[char:char+2]] += 1

    for step in range(steps):
        new_counts = Counter()
        for pair, count in pair_counts.items():
            for new_pair in expanded_rules[pair]:
                new_counts[new_pair] += count
        pair_counts = new_counts

    final_count = Counter()
    for pair, count in pair_counts.items():
        final_count[pair[1]] += count
    final_count[template[0]] += 1

    sorted_elements = final_count.most_common()
    return sorted_elements[0][1] - sorted_elements[-1][1]


if __name__ == '__main__':
    with Timer("Part 1"):
        part1_result = calcElementRange("../input/day_14.txt", 10)
    print(f"Part 1 Result: {part1_result}")
    with Timer("Part 2"):
        part2_result = calcElementRange("../input/day_14.txt", 40)
    print(f"Part 2 Result: {part2_result}")
