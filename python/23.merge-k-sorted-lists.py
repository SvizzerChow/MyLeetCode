from typing import List

from tools.ListNode import ListNode,stringToListNode,listNodeToString


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) <= 2:
            return self.doMerge(lists)
        one = self.mergeKLists(lists[0:len(lists)//2])
        two = self.mergeKLists(lists[len(lists)//2:len(lists)])
        return self.mergeKLists([one, two])

    def doMerge(self, lists):
        head = before = None
        while True:
            node = None
            index = None
            for i in range(len(lists)):
                if node is None or (lists[i] is not None and lists[i].val < node.val):
                    node = lists[i]
                    index = i
            if node is None:
                break
            if head is None:
                head = before = node
            else:
                before.next = node
                before = node
            lists[index] = node.next
            if lists[index] is None:
                del lists[index]
        return head


print(listNodeToString(Solution().mergeKLists([stringToListNode("[1,4,5]"), stringToListNode("[1,3,4]"), stringToListNode("[2,6]")])))