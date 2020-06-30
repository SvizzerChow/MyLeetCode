import random

from tools import ListNode


class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        p = self.head
        i = 0
        result = self.head.val
        while p:
            i += 1
            x = random.randint(1, i)
            if x == i:
                result = p.val
            p = p.next
        return result


x = [0] * 5
s = Solution(ListNode.stringToListNode("[1, 2, 4]"))
for i in range(1000):
    x[s.getRandom()] += 1

print(x)