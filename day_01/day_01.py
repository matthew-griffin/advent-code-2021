from collections import deque


def countWindowedIncreases(input_file, window_size):
    increases = 0
    with open(input_file) as file:
        previous = None
        current = deque(maxlen=window_size)
        for line in file:
            current.appendleft(int(line))
            if previous is not None and sum(current) > sum(previous):
                increases += 1
            if len(current) is window_size:
                previous = current.copy()

    return increases


if __name__ == '__main__':
    basic = countWindowedIncreases("../input/day_01.txt", 1)
    print(f"Increases: {basic}")
    windowed = countWindowedIncreases("../input/day_01.txt", 3)
    print(f"Windowed Increases: {windowed}")
