from tools.ListNode import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        result = None
        p = head
        while p is not None:
            temp = p.next
            p.next = result
            result = p
            p = temp
        return result