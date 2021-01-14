from tools.ListNode import ListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = fast = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


