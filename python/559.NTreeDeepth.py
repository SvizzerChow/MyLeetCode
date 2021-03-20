
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        return self.getMaxLevel(root, 0)

    def getMaxLevel(self, root, level):
        if root is None:
            return level
        level += 1
        if root.children is None:
            return level
        maxLevel = level
        for node in root.children:
            temp = self.getMaxLevel(node, level)
            if temp > maxLevel:
                maxLevel = temp
        return maxLevel