class Solution:
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)
        total = sum(cardPoints)
        s = sum(cardPoints[:n - k])
        res = total - s
        for i in range(n - k, n):
            s += cardPoints[i] - cardPoints[i - (n - k)]
            res = max(res, total - s)
        
        return res
        
a = Solution()
print(a.maxScore([1,79,80,1,1,1,200,1], 8))