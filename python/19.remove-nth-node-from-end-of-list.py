from tools.ListNode import ListNode, stringToListNode, listNodeToString


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return None
        fast = head
        for i in range(n):
            if fast is None:
                return None
            fast = fast.next
        slow = head
        pre = None
        while fast is not None:
            fast = fast.next
            pre = slow
            slow = slow.next
        if pre is None:
            head = slow.next
        else:
            pre.next = slow.next
        return head

node = stringToListNode("[1,2,3,4,5]")
n = 2
print(listNodeToString(Solution().removeNthFromEnd(node, n)))
print("--------------")