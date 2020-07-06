from typing import List

from tools.TreeNode import TreeNode, treeNodeToString


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) < 1:
            return None
        head = TreeNode(-1)
        stack = [[0, len(nums) - 1, head]]
        index = 0
        while index < len(stack):
            position = stack[index]
            p = position[2]
            mid = (position[0] + position[1]) // 2 if (position[1] - position[0]) % 2 == 0 else (position[1] +
                                                                                                 position[
                                                                                                     0]) // 2 + 1
            node = TreeNode(nums[mid])
            if p.left is None:
                p.left = node
            else:
                p.right = node
            if position[0] < mid:
                stack.append([position[0], mid - 1, node])
            if position[1] > mid:
                stack.append([mid + 1, position[1], node])
            index += 1
        return head.left


print(treeNodeToString(Solution().sortedArrayToBST([-10, -3, 0, 5, 9])))
