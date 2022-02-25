class Solution:
    def maxProfit(self, prices):
        dp = [0] * len(prices)
        dp[0] = 0
        m = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < m:
                m = prices[i]
                continue
            else:
                dp[i] = prices[i] - m
        return max(dp)

a = Solution()
print(a.maxProfit([7,6,4,3,1]))