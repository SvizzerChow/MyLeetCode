from typing import List

from tools import TreeNode

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        result = []
        queue = [root]
        while len(queue) > 0:
            length = len(queue)
            temp = [0]*length
            for i in range(length):
                node = queue.pop(0)
                temp[i] = node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result.append(temp)
        return result

print(Solution().levelOrder(TreeNode.stringToTreeNode("[3,9,20,null,null,15,7]")))