from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(list)
        rows = defaultdict(list)
        grids = defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rows[j] or board[i][j] in cols[i] or board[i][j] in grids[(i//3, j//3)]:
                    return False
                rows[j].append(board[i][j])
                cols[i].append(board[i][j])
                grids[(i//3, j//3)].append(board[i][j])
        return True
