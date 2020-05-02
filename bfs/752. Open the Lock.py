import collections
from typing import List


class Solution:
    def convert(self, node):
        res = []
        for i, ch in enumerate(node):
            num = int(ch)
            res.append(node[:i] + str((num - 1) % 10) + node[i + 1:])
            res.append(node[:i] + str((num + 1) % 10) + node[i + 1:])
        return res

    def openLock(self, deadends: List[str], target: str) -> int:
        start, depth = '0000', -1
        visited = set(deadends)
        if start in visited: return depth

        queue = collections.deque([start])

        while queue:
            size = len(queue)
            depth += 1
            for _ in range(size):
                node = queue.popleft()
                if node == target: return depth
                if node in visited: continue
                visited.add(node)
                '''extend(iterable)
                   Extend the right side of the deque by appending elements from the iterable argument.'''
                queue.extend(self.convert(node))
        return -1


if __name__ == '__main__':
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"
    res = Solution().openLock(deadends, target)
    print(res)
