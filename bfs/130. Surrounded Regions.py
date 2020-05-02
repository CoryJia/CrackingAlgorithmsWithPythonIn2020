from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        if not board or not board[0]: return

        row, col = len(board), len(board[0])

        queue = deque()
        for i in range(row):
            queue.append((i, 0))
            queue.append((i, col - 1))

        for j in range(col):
            queue.append((0, j))
            queue.append((row - 1, j))

        while queue:
            i,j = queue.popleft();

            if 0<= i < row and 0<= j < col and board[i][j] == 'O':
                board[i][j] = 'Y'

                queue.append((i - 1, j))
                queue.append((i + 1, j))
                queue.append((i, j - 1))
                queue.append((i, j + 1))


        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'Y':
                    board[i][j] = 'O'