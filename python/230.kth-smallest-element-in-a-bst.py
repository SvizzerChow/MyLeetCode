from tools.TreeNode import TreeNode, stringToTreeNode


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return self._kthSmallest(root, k)[1]

    def _kthSmallest(self, root, k):
        result = [k, None]
        if root.left is not None:
            result = self._kthSmallest(root.left, k)
            if result[0] == 0:
                return result
        result[0] -= 1
        if result[0] == 0:
            result[1] = root.val
            return result
        if root.right is not None:
            result = self._kthSmallest(root.right, result[0])
            if result[0] == 0:
                return result
        return result


print(Solution().kthSmallest(stringToTreeNode("[5,3,6,2,4,null,null,1]"), 3))