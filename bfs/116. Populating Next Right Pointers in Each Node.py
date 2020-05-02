class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cur = root

        while cur and cur.left:
            next = cur.left

            while cur:
                cur.left.next = cur.right
                cur.right.next = cur.next and cur.next.left
                cur = cur.next
            cur = next
        return root