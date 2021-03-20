from tools import TreeNode

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.dfs(root, None) is not None

    def dfs(self, root, before):
        last = None
        if root.left is not None:
            temp = self.dfs(root.left, before)
            if temp is None or temp >= root.val:
                return None
        if before is None or root.val > before:
            last = root.val
        else:
            return None
        if root.right is not None:
            temp = self.dfs(root.right, last)
            if temp is None or temp <= root.val:
                return None
            last = temp
        return last





print(Solution().isValidBST(TreeNode.stringToTreeNode("[5,1,4,null,null,3,6]")))