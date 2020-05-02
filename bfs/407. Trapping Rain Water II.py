from heapq import *
from typing import List


class Cell(object):
    def __init__(self, i, j, height):
        self.i = i
        self.j = j
        self.height = height

    def __lt__(self, other):
        return self.height < other.height


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        row = len(heightMap)
        if row <= 2: return 0

        col = len(heightMap[0])
        if col <= 2: return 0

        heap, visited = [], set()

        for i in 0, row - 1:
            for j in range(col):
                heap.append(Cell(i, j, heightMap[i][j]))
                visited.add((i, j))

        for j in 0, col - 1:
            for i in range(row):
                heap.append(Cell(i, j, heightMap[i][j]))
                visited.add((i, j))

        heapify(heap)
        max_height, water = 0, 0

        while heap:
            cur = heappop(heap)

            i, j, cur_height = cur.i, cur.j, cur.height

            if cur_height > max_height:
                max_height = cur_height
            else:
                water += max_height - cur_height

            for ii, jj in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= ii < row and  0 <= jj < col and (ii, jj) not in visited:
                   heappush(heap, Cell(ii, jj, heightMap[ii][jj]))
                   visited.add((ii, jj))
        return water

if __name__ == '__main__':
    heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
    print(Solution().trapRainWater(heightMap))