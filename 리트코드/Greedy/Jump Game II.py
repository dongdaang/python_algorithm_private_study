class Solution:
    def jump(self, nums):
        dp = [0] * 10000
        if len(nums) == 1:
            return 0
        for i in range(len(nums)):
            j = i + 1
            while j < i + nums[i] + 1 and j < len(nums):
                if dp[j] == 0:
                    dp[j] += dp[i] + 1
                else:
                    dp[j] = min(dp[j], dp[i] + 1)
                j += 1
        return dp[len(nums) - 1]
a = Solution()
print(a.jump([1,1,1,1]))


###############빠른 코드###############
# 
# def jump(self, nums):
#         if len(nums) <= 1: return 0
#         l, r = 0, nums[0]
#         times = 1
#         while r < len(nums) - 1:
#             times += 1
#             nxt = max(i + nums[i] for i in range(l, r + 1))   뛸 수 있는 범위 내에서
#             l, r = r, nxt                                     그 다음으로 뛸 수 있는 최대 위치 찾기
#         return times