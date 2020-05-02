# 317. Shortest Distance from All Buildings
import collections
from typing import List


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        self.cost = [[None] * col for _ in range(row)]

        buildings = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    self.visited = set((i, j))
                    self.bfs(i, j, grid)
                    buildings += 1

        min_dist = float("inf")

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0 and self.cost[i][j] and len(self.cost[i][j]) == buildings:
                    min_dist = min(min_dist, sum(self.cost[i][j]))

        return min_dist if min_dist != float("inf") else -1

    def bfs(self, x, y, grid):
        queue = collections.deque([(x, y, 0)])

        while queue:
            i, j, move = queue.popleft()

            for nx, ny in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if (nx, ny) not in self.visited and 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][
                    ny] == 0:
                    self.visited.add((nx, ny))
                    if not self.cost[nx][ny]:
                        self.cost[nx][ny] = [move + 1]
                    else:
                        self.cost[nx][ny].append(move + 1)
                    queue.append((nx, ny, move + 1))
