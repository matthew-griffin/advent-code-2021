from src.timer import Timer

CHUNK_PAIRS = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

ERROR_SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

COMPLETION_SCORES = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}


def calcSyntaxErrorScore(input_file):
    score = 0
    with open(input_file) as file:
        for line in file:
            expected_closes = []
            for char in line.strip():
                if char in CHUNK_PAIRS:
                    expected_closes.append(CHUNK_PAIRS[char])
                elif expected_closes and char != expected_closes.pop():
                    score += ERROR_SCORES[char]
                    break
    return score


def calcMiddleCompleteScore(input_file):
    scores = []
    with open(input_file) as file:
        for line in file:
            expected_closes = []
            needs_complete = True
            for char in line.strip():
                if char in CHUNK_PAIRS:
                    expected_closes.append(CHUNK_PAIRS[char])
                elif expected_closes and char != expected_closes.pop():
                    needs_complete = False
                    break
            if needs_complete:
                score = 0
                while expected_closes:
                    score = score * 5 + COMPLETION_SCORES[expected_closes.pop()]
                scores.append(score)
    scores = sorted(scores)
    return scores[len(scores)//2]


if __name__ == '__main__':
    with Timer("Part 1"):
        part1_result = calcSyntaxErrorScore("../input/day_10.txt")
    print(f"Part 1 Result: {part1_result}")
    with Timer("Part 2"):
        part2_result = calcMiddleCompleteScore("../input/day_10.txt")
    print(f"Part 2 Result: {part2_result}")
