class Solution:
    def minSubArrayLen(self, target, nums):
        if sum(nums) < target:
            return 0
        l, r = 0, 0
        s = nums[0]
        res = len(nums)
        while l <= r:
            if r == len(nums) - 1 and s < target:
                break
            if s >= target:
                res = min(res, r - l + 1)
                s -= nums[l]
                l += 1
            else:
                r += 1
                s += nums[r]
        return res
a = Solution()
print(a.minSubArrayLen(7, [2,3,1,2,4,3]))