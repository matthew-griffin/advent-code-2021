from src.timer import Timer

class Board:
    class Entry:
        def __init__(self, value):
            self.value = value
            self.marked = False

    def __init__(self):
        self.rows = [[], [], [], [], []]
        self.lookup = {}
        self.next_row = 0
        self.next_column = 0

    def addEntry(self, value):
        self.rows[self.next_row].append(Board.Entry(value))
        self.lookup[value] = (self.next_row, self.next_column)
        self.next_column += 1
        if self.next_column > 4:
            self.next_column = 0
            self.next_row += 1

    def markEntry(self, value):
        if value in self.lookup:
            (row, column) = self.lookup[value]
            self.rows[row][column].marked = True

    def isWinner(self):
        all_col_marked = [True, True, True, True, True]
        for row in self.rows:
            all_row_marked = True
            for index, entry in enumerate(row):
                if not entry.marked:
                    all_row_marked = False
                    all_col_marked[index] = False
            if all_row_marked:
                return True
        for col in all_col_marked:
            if col:
                return True
        return False

    def calcSumUnmarked(self):
        result = 0
        for row in self.rows:
            for entry in row:
                result += entry.value if not entry.marked else 0
        return result


def createDrawAndBoards(input_file):
    boards = []
    with open(input_file) as file:
        line = file.readline()
        draw_order = [int(num) for num in line.split(',')]
        new_board = None
        while line:
            line = file.readline()
            row = line.split()
            if row:
                for entry in row:
                    new_board.addEntry(int(entry))
            else:
                if new_board is not None:
                    boards.append(new_board)
                new_board = Board()
    return draw_order, boards


def findWinningBoardProduct(input_file):
    draw_order, boards = createDrawAndBoards(input_file)

    for drawn in draw_order:
        for board in boards:
            board.markEntry(drawn)
            if board.isWinner():
                return board.calcSumUnmarked() * drawn

    return 0


def findLastWinningBoardProduct(input_file):
    draw_order, boards = createDrawAndBoards(input_file)

    for drawn in draw_order:
        for board in boards:
            board.markEntry(drawn)
        if len(boards) is 1 and boards[0].isWinner():
            return boards[0].calcSumUnmarked() * drawn
        boards = [board for board in boards if not board.isWinner()]
    return 0


if __name__ == '__main__':
    with Timer("Part 1"):
        part1_result = findWinningBoardProduct("../input/day_04.txt")
    print(f"Part 1 Result: {part1_result}")
    with Timer("Part 2"):
        part2_result = findLastWinningBoardProduct("../input/day_04.txt")
    print(f"Part 2 Result: {part2_result}")
