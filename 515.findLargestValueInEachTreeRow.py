from typing import List

from tools import TreeNode

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        result = []
        queue = [root]
        while len(queue) > 0:
            maxValue = None
            length = len(queue)
            for i in range(length):
                node = queue.pop(0)
                if maxValue is None or maxValue < node.val:
                    maxValue = node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result.append(maxValue)
        return result

print(Solution().largestValues(TreeNode.stringToTreeNode("[1,3,2,5,3,9]")))

