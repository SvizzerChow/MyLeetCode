 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        dfs1 = self.getDFS(s)
        dfs2 = self.getDFS(t)
        i = 0
        while i < len(dfs1):
            if dfs1[i] == dfs2[0]:
                flag = True
                for k in range(len(dfs2)):
                    if dfs1[i+k] !=  dfs2[k]:
                        flag = False
                        break
                if flag:
                    return True
            i = i + 1
        return False

    def getDFS(self, s): 
        if s is None:
            return [self.dNone(s)]
        x = [self.dNone(str(s.val))]
        x.extend(self.getDFS(s.left))
        x.extend(self.getDFS(s.right))
        return x


    def dNone(self, s):
        if s is None:
            return "_"
        return s