from tools import ListNode


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        if length <= 1:
            return head
        count = 0
        pre = None
        node = head
        while count < length // 2:
            count += 1
            pre = node
            node = node.next
        pre.next = None
        before = self.sortList(head)
        if node:
            after = self.sortList(node)
            node = before
            pre = None
            while after:
                temp = after.next
                while node:
                    if node.val >= after.val:
                        if pre:
                            pre.next = after
                        else:
                            before = after
                        after.next = node
                        pre = after
                        break
                    pre = node
                    node = node.next
                if not node:
                    pre.next = after
                    pre = after
                    after.next = None
                after = temp
        return before


print(ListNode.listNodeToString(Solution().sortList(ListNode.stringToListNode("[-1,5,3,4,0]"))))






