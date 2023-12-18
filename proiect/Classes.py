class Game:
    def __init__(self, rows, columns, current_player, player1, player2):
        self.board = Board(rows, columns)
        self.current_player = current_player
        self.player1 = player1
        self.player2 = player2
        self.winner = None

    def no_more_moves(self):
        for row in range(self.board.rows - 1):
            for col in range(self.board.columns - 1):
                if self.board.matrix[row][col] == 0:
                    return False
        return True

    def change_current_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def get_opponent(self):
        if self.current_player == self.player1:
            return self.player2
        else:
            return self.player1

    def winner_found(self):
        if self.board.found_4_in_a_row(self.player1.color):
            self.winner = self.player1
            return True
        elif self.board.found_4_in_a_row(self.player2.color):
            self.winner = self.player2
            return True
        return False


class Player:
    def __init__(self, color, role):
        self.color = color
        self.role = role


class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = [[0 for _ in range(columns)] for _ in range(rows)]

    def __getitem__(self, index):
        return self.matrix[index]

    def print_board(self):
        for row in self.matrix:
            print(row)
        print("\n")

    def remove_disc(self, col):
        for row in range(self.rows):
            if self.matrix[row][col] != 0:
                self.matrix[row][col] = 0
                return

    def found_4_in_a_row(self, target):
        # Check horizontally
        for row in self.matrix:
            for i in range(self.columns - 3):
                if all(element == target for element in row[i:i + 4]):
                    return True

        # Check vertically
        for j in range(self.columns):
            for i in range(self.rows - 3):
                if all(self.matrix[i + k][j] == target for k in range(4)):
                    return True

        # Check diagonally (from top-left to bottom-right)
        for i in range(self.rows - 3):
            for j in range(self.columns - 3):
                if all(self.matrix[i + k][j + k] == target for k in range(4)):
                    return True

        # Check diagonally (from top-right to bottom-left)
        for i in range(self.rows - 3):
            for j in range(3, self.columns):
                if all(self.matrix[i + k][j - k] == target for k in range(4)):
                    return True

        return False

    def is_valid_move(self, col_to_put_disc):
        if col_to_put_disc > self.columns - 1:
            return False
        if self.matrix[0][col_to_put_disc] != 0:
            return False
        return True

    def add_disc(self, player, col_to_put_disc):
        if self.is_valid_move(col_to_put_disc):
            added = False
            i = self.rows - 1
            while not added:
                if self.matrix[i][col_to_put_disc] == 0:
                    self.matrix[i][col_to_put_disc] = player.color
                    added = True
                else:
                    i -= 1
            return added
        else:
            return False
