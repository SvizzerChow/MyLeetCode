from tools.TreeNode import TreeNode
from tools.TreeNode import stringToTreeNode
from tools.TreeNode import treeNodeToString

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        n = TreeNode(None)
        self.change(root, n)
        return n.right

    def change(self, root, father):
        if root.left is not None:
            father = self.change(root.left, father)
        if father is None:
            father = TreeNode(root.val)
        else:
            father.right = TreeNode(root.val)
            father = father.right
        if root.right is not None:
            father = self.change(root.right, father)
        return father

print(treeNodeToString(Solution().increasingBST(stringToTreeNode("[5,3,6,2,4,null,8,1,null,null,null,7,9]"))))