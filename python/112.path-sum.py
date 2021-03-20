from tools import TreeNode


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        return self._addValEqual(root, 0, sum)

    def _addValEqual(self, node, counter, sum):
        if node is None:
            return counter == sum
        counter += node.val
        haveChild = False
        if node.left is not None:
            haveChild = True
            if self._addValEqual(node.left, counter, sum):
                return True
        if node.right is not None:
            haveChild = True
            if self._addValEqual(node.right, counter, sum):
                return True
        return False if haveChild else counter == sum


print(Solution().hasPathSum(TreeNode.stringToTreeNode("[0,1,1]"), 0))