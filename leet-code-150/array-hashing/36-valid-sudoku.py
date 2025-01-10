"""
Collect the set of things we see, encoded as strings. For example:

'4' in row 7 is encoded as "(4)7".
'4' in column 7 is encoded as "7(4)".
'4' in the top-right block is encoded as "0(4)2".
Scream false if we ever fail to add something because it was already added (i.e., seen before).

public boolean isValidSudoku(char[][] board) {
    Set seen = new HashSet();
    for (int i=0; i<9; ++i) {
        for (int j=0; j<9; ++j) {
            if (board[i][j] != '.') {
                String b = "(" + board[i][j] + ")";
                if (!seen.add(b + i) || !seen.add(j + b) || !seen.add(i/3 + b + j/3))
                    return false;
            }
        }
    }
    return true;
}
"""


def isValidSudoku(self, board):
    return (
        self.is_row_valid(board)
        and self.is_col_valid(board)
        and self.is_square_valid(board)
    )


def is_row_valid(self, board):
    for row in board:
        if not self.is_unit_valid(row):
            return False
    return True


def is_col_valid(self, board):
    for col in zip(*board):
        if not self.is_unit_valid(col):
            return False
    return True


def is_square_valid(self, board):
    for i in (0, 3, 6):
        for j in (0, 3, 6):
            square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not self.is_unit_valid(square):
                return False
    return True


def is_unit_valid(self, unit):
    unit = [i for i in unit if i != "."]
    return len(set(unit)) == len(unit)
