from tools.ListNode import ListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = head
        fast = slow.next
        slowAdd = False
        while True:
            if fast is None:
                return False
            if fast == slow:
                return True
            fast = fast.next
            if slowAdd:
                slow = slow.next
                slowAdd = False
            else:
                slowAdd = True

