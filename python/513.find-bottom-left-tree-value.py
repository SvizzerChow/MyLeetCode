from tools import TreeNode

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        return self.getLastLeft(root, 0)[1]

    def getLastLeft(self, root: TreeNode, level):
        x = [level, root.val]
        if root.left is not None:
            x = self.getLastLeft(root.left, level+1)
        if root.right is not None:
            temp = self.getLastLeft(root.right, level+1)
            if x[0] < temp[0]:
                x = temp
        return x