import sys

from tools.TreeNode import TreeNode, stringToTreeNode


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        result = self.maxPathSumDfs(root)
        return max(result[0], result[1])

    def maxPathSumDfs(self, root: TreeNode):
        if root is None:
            return [0, -sys.maxsize]
        left = self.maxPathSumDfs(root.left)
        right = self.maxPathSumDfs(root.right)
        path = max(root.val, root.val + left[0], root.val + right[0])
        return [path, max(path, root.val + left[0] + right[0], left[1], right[1])]





print(Solution().maxPathSum(stringToTreeNode("[2, -1, -2]")))
