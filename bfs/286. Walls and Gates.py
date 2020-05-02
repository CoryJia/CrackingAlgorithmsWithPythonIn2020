import collections
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        # edge case
        if not rooms:
            return

        INF, row, col, DIR, queue = 2 ** 31 - 1, len(rooms), len(rooms[0]), [[1, 0], [-1, 0], [0, 1],
                                                                             [0, -1]], collections.deque()

        for i in range(row):
            for j in range(col):
                if rooms[i][j] == 0:
                    queue.append(i, j)

        while queue:
            top = queue.popleft()
            i, j = top[0], top[1]

            for dir in DIR:
                ii, jj = dir[0] + i, dir[1] + j

                if 0 <= ii < row and 0 <= jj < col and rooms[ii][jj] == INF:
                    rooms[ii][jj] = rooms[i][j] + 1
                    queue.append(ii, jj)
