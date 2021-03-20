from tools.ListNode import ListNode


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        before = None
        after = None
        result = None
        p = head
        counter = 0
        while p is not None:
            temp = p.next
            counter += 1
            if counter < m:
                before = p
            elif counter > n:
                after.next = p
                break
            else:
                if after is None:
                    after = p
                p.next = result
                result = p
            p = temp
        if before is not None:
            before.next = result
            result = head
        return result
