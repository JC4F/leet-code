"""
Input:
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "CAT"

Output: true
"""

"""
1. Backtracking (Hash Set)
Time complexity: O(m*n*4^k), where m is the number of rows, n is the number of columns, and k is the length of the word
Space complexity: O(n)
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (
                min(r, c) < 0
                or r >= ROWS
                or c >= COLS
                or word[i] != board[r][c]
                or (r, c) in path
            ):
                return False

            path.add((r, c))
            res = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False


"""
2. Backtracking (Visited Array)
Time complexity: O(m*n*4^k), where m is the number of rows, n is the number of columns, and k is the length of the word
Space complexity: O(n)
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (
                r < 0
                or c < 0
                or r >= ROWS
                or c >= COLS
                or word[i] != board[r][c]
                or visited[r][c]
            ):
                return False

            visited[r][c] = True
            res = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            visited[r][c] = False
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False


"""
3. Backtracking (Optimal)
Time complexity: O(m*n*4^k), where m is the number of rows, n is the number of columns, and k is the length of the word
Space complexity: O(n)
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (
                r < 0
                or c < 0
                or r >= ROWS
                or c >= COLS
                or word[i] != board[r][c]
                or board[r][c] == "#"
            ):
                return False

            board[r][c] = "#"
            res = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            board[r][c] = word[i]
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
