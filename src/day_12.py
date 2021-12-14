from collections import defaultdict, Counter

from src.timer import Timer


def populateGraph(input_file):
    graph = defaultdict(set)
    with open(input_file) as file:
        for line in file:
            node_pair = line.strip().split('-')
            graph[node_pair[0]].add(node_pair[1])
            graph[node_pair[1]].add(node_pair[0])
    return graph


def recCalcNumPaths(graph, path_stack, block_cave_check):
    path_count = 0
    current_node = graph[path_stack[-1]]
    containsSmallCaveLoop = 2 in Counter([x for x in path_stack if x.islower()]).values()
    for connection in current_node:
        if connection == "start":
            continue
        if connection == "end":
            path_count += 1
            continue
        if connection.islower() and block_cave_check(connection, containsSmallCaveLoop):
            continue

        path_stack.append(connection)
        path_count += recCalcNumPaths(graph, path_stack, block_cave_check)
        path_stack.pop()
    return path_count


def calcNumPaths(input_file):
    graph = populateGraph(input_file)
    path_stack = ["start"]
    return recCalcNumPaths(graph, path_stack, lambda a, b: a in path_stack)


def calcNumPathsRepeatSmallCave(input_file):
    graph = populateGraph(input_file)
    path_stack = ["start"]
    return recCalcNumPaths(graph, path_stack, lambda a, b: a in path_stack and b)


if __name__ == '__main__':
    with Timer("Part 1"):
        part1_result = calcNumPaths("../input/day_12.txt")
    print(f"Part 1 Result: {part1_result}")
    with Timer("Part 2"):
        part2_result = calcNumPathsRepeatSmallCave("../input/day_12.txt")
    print(f"Part 2 Result: {part2_result}")
