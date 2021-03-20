from tools import  TreeNode

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        self.doPruneTree(root)
        return root

    def doPruneTree(self, root):
        flag = False
        if root.left is not None:
            x = self.doPruneTree(root.left)
            if not x:
                root.left = None
            flag = flag or x
        if root.right is not None:
            x = self.doPruneTree(root.right)
            if not x:
                root.right = None
            flag = flag or x
        return flag or (root.val == 1)

print(TreeNode.treeNodeToString(Solution().pruneTree(TreeNode.stringToTreeNode("[1,null,0,0,1]"))))

