from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        visited = set()
        q = deque()
        row, col = len(matrix), len(matrix[0])

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    visited.add((i, j))
                    q.append((i, j))

        while q:
            i, j = q.popleft()
            for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ii, jj = i + dir[0], j + dir[1]

                if 0<= ii < row and 0<= jj < col and (ii, jj) not in visited:
                    matrix[ii][jj] = matrix[i][j] + 1
                    visited.add((ii, jj))
                    q.append((ii, jj))
        return matrix