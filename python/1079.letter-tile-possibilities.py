class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        length = len(tiles)
        if length < 1:
            return 0
        tMap = {}
        for i in tiles:
            if tMap.get(i) is not None:
                tMap[i] = tMap[i] + 1
            else:
                tMap[i]=1
        return self._dfs(tMap)

    def _dfs(self, tMap):
        count = 0
        for key in tMap.keys():
            if tMap[key] == 0:
                continue
            tMap[key] = tMap[key] - 1
            count += 1
            count += self._dfs(tMap)
            tMap[key] = tMap[key] + 1
        return count



print(Solution().numTilePossibilities("AAAB"))