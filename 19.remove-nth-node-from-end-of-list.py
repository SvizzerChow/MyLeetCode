from tools.ListNode import ListNode, stringToListNode, listNodeToString


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l = []
        p = head
        while p is not None:
            l.append(p)
            p = p.next
        end = l[-n+1] if n > 1 else None
        before = l[-n-1] if len(l) - n - 1 >=0 else None
        if before:
            before.next = end
        else:
            head = end
        return head


node = stringToListNode("[1,2,3,4,5]")
n = 2
print(listNodeToString(Solution().removeNthFromEnd(node, n)))
print("--------------")