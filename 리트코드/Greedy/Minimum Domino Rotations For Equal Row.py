#https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/


class Solution:
    def minDominoRotations(self, tops, bottoms):
        n = len(tops)
        cnt = 0
        a = tops[0]
        b = bottoms[0]
        for i in range(1, n):
            if bottoms[i] == b or tops[i] == a:
                continue
            if bottoms[i] == a or tops[i] == b:
                tops[i], bottoms[i] = bottoms[i], tops[i]
                cnt += 1
            else:
                return -1
        flag1 = True
        flag2 = True
        for i in tops:
            if i != a:
                flag1 = False
                break
        if flag1:
            if cnt > n // 2:
                return n - cnt
            else:
                return cnt
        for i in bottoms:
            if i != b:
                flag2 = False
                break
        if flag2:
            if cnt > n // 2:
                return n - cnt
            else:
                return cnt
        return -1

a = Solution()
print(a.minDominoRotations([1,2,2,1,2,1,2,1,2], [1,2,1,1,1,1,2,1,2]))