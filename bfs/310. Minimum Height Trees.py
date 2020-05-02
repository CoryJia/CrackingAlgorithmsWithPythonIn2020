#310. Minimum Height Trees
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [set() for _ in range(n)]

        for u, v in edges:
            graph[u].add(v);
            graph[v].add(u);

        leaves = [x for x in range(n) if len(graph[x]) <= 1]
        pre_leaves = leaves

        while leaves:
            new_leaves = []

            for leaf in leaves:
                if not graph[leaf]:
                    return leaves
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            pre_leaves, leaves = leaves, new_leaves

        return pre_leaves