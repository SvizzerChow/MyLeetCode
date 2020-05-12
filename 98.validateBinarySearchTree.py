from tools import TreeNode

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.dfsMax(root) is not None

    def dfsMax(self, root):
        maxValue = root.val
        minValue = root.val
        if root.left is not None:
            value = self.dfsMax(root.left)
            if value is None or (value[0] >= root.val or value[1] >= root.val):
                return None
            minValue = value[0]
        if root.right is not None:
            value = self.dfsMax(root.right)
            if value is None or (value[0] <= root.val or value[1] <= root.val):
                return None
            maxValue = value[1]
        return [minValue, maxValue]

    def check(self, value, val):
        if value[0] >=val:
            return True
        if value[1] <= val:
            return True
        return False


print(Solution().isValidBST(TreeNode.stringToTreeNode("[10,5,15,null,null,6,20]")))