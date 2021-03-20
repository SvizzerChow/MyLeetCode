from tools.TreeNode import TreeNode, stringToTreeNode, treeNodeToString


class Solution:
    def flatten(self, root: TreeNode) -> None:
        if root is None:
            return
        self._dfs(root)

    def _dfs(self, root):
        right = root.right
        node = root
        if root.left is not None:
            node = self._dfs(root.left)
            root.right = root.left
            root.left = None
        if right is not None:
            temp = self._dfs(right)
            node.right = right
            node = temp
        return node





node = stringToTreeNode("[1,2,5,3,4,null,6]")
Solution().flatten(node)
print(treeNodeToString(node))
