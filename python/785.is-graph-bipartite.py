import collections
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        length = len(graph)
        flag = [None] * length
        for i in range(length):
            if flag[i] is None:
                flag[i] = 1
                queue = collections.deque([i])
                while queue:
                    node = queue.popleft()
                    nextColor = 2 if flag[node] == 1 else 1
                    for n in graph[node]:
                        if flag[n] is None:
                            flag[n] = nextColor
                            queue.append(n)
                        elif flag[n] != nextColor:
                            return False
        return True


print(Solution().isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))



