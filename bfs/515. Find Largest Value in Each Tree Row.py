import collections
from typing import List

from adt.TreeNode import TreeNode


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        queue = collections.deque([root])

        while queue:
            res.append(max(x.val for x in queue))

            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
        return res