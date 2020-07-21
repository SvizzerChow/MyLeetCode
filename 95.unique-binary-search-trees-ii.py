from typing import List

from tools.TreeNode import TreeNode, treeNodeToString


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        left = [None for _ in range(n+1)]
        if n > 0:
            left[1] = [TreeNode(1)]
        right = [None for _ in range(n+1)]
        if n > 0:
            right[n] = [TreeNode(n)]
        return self._generateTrees(1, n, left, right, 1, n)

    def _generateTrees(self, start, end, left, right, s, e):
        if end - start == 0:
            return [TreeNode(start)]
        result = []
        for i in range(start, end+1):
            leftNodes = []
            rightNodes = []
            if start < i:
                if start == s and left[i-1] is not None:
                    leftNodes = left[i-1]
                else:
                    leftNodes = self._generateTrees(start, i-1, left, right, s, e)
                    if start == s:
                        left[i-1] = leftNodes
            if i < end:
                if end == e and right[i+1] is not None:
                    rightNodes = right[i+1]
                else:
                    rightNodes = self._generateTrees(i+1, end, left, right, s, e)
                    if end == e:
                        right[i+1] = rightNodes
            indexLeft, indexRight = 0, 0
            while indexLeft < len(leftNodes) or indexRight < len(rightNodes):
                temp = TreeNode(i)
                if indexLeft < len(leftNodes):
                    temp.left = leftNodes[indexLeft]
                if indexRight < len(rightNodes):
                    temp.right = rightNodes[indexRight]
                    indexRight += 1
                result.append(temp)
                if indexLeft == (len(leftNodes)-1) and indexRight == len(rightNodes):
                    break
                if indexLeft < len(leftNodes) and indexRight == len(rightNodes):
                    indexRight = 0
                    indexLeft += 1
        return result


result = Solution().generateTrees(4)
for r in result:
    print("- "+treeNodeToString(r))