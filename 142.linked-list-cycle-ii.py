from tools.ListNode import ListNode


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while True:
            if fast is None or fast.next is None:
                return None
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                break
        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow
