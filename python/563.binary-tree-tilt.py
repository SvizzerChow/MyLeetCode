from tools import TreeNode


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if root is None:
            return 0
        result = [0]
        self.getSum(root, result)
        return result[0]


    def getSum(self, root, num):
        sumLeft = 0
        sumRight = 0
        if root.left is not None:
            sumLeft = self.getSum(root.left, num)
        if root.right is not None:
            sumRight = self.getSum(root.right, num)
        num[0] = num[0] + abs(sumLeft - sumRight)
        return sumLeft + sumRight + root.val


root = TreeNode.stringToTreeNode("[1,2,3]")

print(Solution().findTilt(root))