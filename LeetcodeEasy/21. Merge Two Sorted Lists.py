from adt import ListNode


class Solution:
    def mergeTwoLists(self, l1:ListNode, l2:ListNode) -> ListNode:
        head = dummy = ListNode(0) #create a dummy node

        while l1 and l2:
            if l1.val <= l2.val:
                temp = l1
                l1 = l1.next
            else:
                temp = l2
                l2 = l2.next

            dummy.next = temp
            dummy = dummy.next

        if l1: dummy.next = l1
        if l2: dummy.next = l2

        return head.next

