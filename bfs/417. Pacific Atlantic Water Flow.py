import collections
from typing import List


class Solution:

    # By DFS
    def pacificAtlanticByDfs(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return []

        p_visited = set()
        a_visited = set()
        rows, cols = len(matrix), len(matrix[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def traverse(i: int, j: int, visited: List[List[int]]):
            if (i, j) in visited: return

            visited.add((i, j))

            for dir in DIRECTIONS:
                ii, jj = i + dir[0], j + dir[1]

                if 0 <= ii < rows and 0 <= jj < cols and matrix[i][j] <= matrix[ii][jj]:
                    traverse(ii, jj, visited)

        for i in range(rows):
            traverse(i, 0, p_visited)
            traverse(i, cols - 1, a_visited)

        for j in range(cols):
            traverse(0, j, p_visited)
            traverse(rows - 1, j, a_visited)

        return list(p_visited & a_visited)

    # By BFS
    def pacificAtlanticByBfs(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        if not matrix: return res

        rows, cols = len(matrix), len(matrix[0])

        pacific = [[False] * cols for _ in range(rows)]
        atlantic = [[False] * cols for _ in range[rows]]

        queue_p = collections.deque()
        queue_a = collections.deque()

        for i in range(rows):
            pacific[i][0] = True
            queue_p.append((i, 0))
            atlantic[i][cols - 1] = True
            queue_a.append((i, cols - 1))

        for j in range(1, cols - 1):
            pacific[0][j] = True
            queue_p.append((0, j))
            atlantic[rows - 1][j] = True
            queue_a.append((rows - 1, j))

        # Add in the edges
        pacific[0][cols - 1] = True
        queue_p.append((0, cols - 1))
        atlantic[rows - 1][0] = True
        queue_a.append((rows - 1, 0))

        self.bfs(matrix, pacific, queue_p, rows, cols)
        self.bfs(matrix, atlantic, queue_a, rows, cols)

        for i in range(rows):
            for j in range(cols):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])

        return res

    def bfs(self, matrix: List[List[int]], seen: List[List[bool]], queue, rows: int, cols: int) -> None:
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        while queue:
            (i, j) = queue.popleft()

            for a, b in DIRECTIONS:
                ii = i + a
                jj = j + b

                if 0 <= ii < rows and 0 <= jj < cols and not seen[ii][jj] and matrix[i][j] <= matrix[ii][jj]:
                    seen[ii][jj] = True
                    queue.append((ii, jj))

    # DFS Template to solve matrix questions
    def dfs(self, matrix):
        # 1. Check for an empty graph.
        if not matrix:
            return []

        # 2. Initialize
        rows, cols = len(matrix), len(matrix[0])
        visited = set()
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def traverse(i, j):
            # a. Check if visited
            if (i, j) in visited:
                return

            # b. Else add to visited
            visited.add((i, j))

            # c. Traverse neighbors
            for dir in DIRECTIONS:
                ii, jj = i + dir[0], j + dir[1]

                if 0 <= ii < rows and 0 <= jj < cols:
                    traverse(ii, jj)

        # 3. Traverse every point in the matrix
        for i in range(rows):
            for j in range(cols):
                traverse(i, j)

    # shortest and longest sentence lengths
    def sentence_lengths(sentences):
        lengths = [len(s.split()) for s in sentences]
        return min(lengths), max(lengths)

    # clean a list of lines
    def clean_lines(lines):
        cleaned = list()
        # prepare regex for char filtering




