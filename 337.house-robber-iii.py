from tools.TreeNode import TreeNode


class Solution:
    def rob(self, root: TreeNode) -> int:
        result = self.rodNode(root)
        return max(result[0], result[1])

    def rodNode(self, root):
        # [root打劫了， root 没有打劫]
        if root is None:
            return [0, 0]
        left = self.rodNode(root.left)
        right = self.rodNode(root.right)
        return [max(left[0]+right[0], left[1] + root.val + right[1]), left[0]+right[0]]
