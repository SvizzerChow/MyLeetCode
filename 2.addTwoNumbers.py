class Solution:
    def addTwoNumbers(self, l1, l2):
        result = None
        rTemp = result
        node1 = l1.next
        node2 = l2.next
        temp = 0
        while node1:
            if node2:
                ad = node1.val+node2.val +temp
            else:
                ad = node1.val +temp
            n = ListNode(ad % 10)
            if rTemp:
                rTemp.next = n 
            else:
                result = n
            rTemp = n
            temp = ad // 10
            node1 = node1.next
        while node2:
            ad = node2.val +temp
            n = ListNode(ad % 10)
            if rTemp:
                rTemp.next = n 
            else:
                result = n
            rTemp = n
            temp = ad // 10
            node2 = node2.next
        return result
l1 = [1,2,3,5]
l2 = [9,2,9]

s = Solution()

print(s.addTwoNumbers(l1,l2))
