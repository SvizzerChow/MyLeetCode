from tools.ListNode import ListNode


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        slow = fast = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow