#https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

class Solution:
    def minDominoRotations(self, tops, bottoms):
        for x in [tops[0],bottoms[0]]:
            if all(x in d for d in zip(tops, bottoms)):
                return len(tops) - max(tops.count(x), bottoms.count(x))
        return -1
            
a = Solution()
print(a.minDominoRotations([1,2,1,1,1,2,2,2],[2,1,2,2,2,2,2,2]))