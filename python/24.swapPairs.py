class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        preBefore = None
        before = None
        start = head
        first = True
        result = None
        while start is not None:
            next = start.next
            if before is None:
                before = start
            else:
                start.next = before
                before.next = next
                if preBefore is not None:
                    preBefore.next = start
                preBefore = before
                before = None
                if first:
                    result = start
                    first = False
            start = next
        if before is not None and preBefore is not None:
            preBefore.next = before
        return result

s =Solution()

print(s.swapPairs)
