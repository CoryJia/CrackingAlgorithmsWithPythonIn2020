from adt.TreeNode import TreeNode


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = [root]
        while queue:
            cur = queue.pop(0)
            res = cur.val

            if cur.right:
                queue.append(cur.right)
            if cur.left:
                queue.append(cur.left)
        return res