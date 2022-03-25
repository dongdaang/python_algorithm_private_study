class Solution:
    def rob(self, nums):
        N = len(nums)
        if N == 1:
            return nums[0]
        elif N == 2:
            return max(nums)
        dp1 = [0] * N
        dp2 = [0] * N
        
        dp1[0] = nums[0]
        dp1[1] = dp1[0]
        dp2[0] = 0
        dp2[1] = nums[1]
        for i in range(2, N - 1):
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i])
        for i in range(2, N):
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i])
        dp1[N - 1] = dp1[N - 2]
        
        return max(dp1[N - 1], dp2[N - 1])
    
a = Solution()
print(a.rob([1,2,3]))