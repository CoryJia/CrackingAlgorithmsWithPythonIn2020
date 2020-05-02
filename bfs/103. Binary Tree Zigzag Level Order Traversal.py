import collections
from typing import List

from adt import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        queue = collections.deque([(root, 0)])

        while queue:
            node, lev = queue.popleft()

            if len(res) < lev + 1:
                res.append([])

            if lev % 2 == 0:
                res[lev].append(node.val)
            else:
                res[lev].insert(0, node.val)

            if node.left: queue.append((node.left, lev + 1))
            if node.right: queue.append((node.right, lev + 1))
        return res
