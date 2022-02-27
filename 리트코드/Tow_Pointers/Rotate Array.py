##############투 포인터 사용##############


class Solution:
    def rotate(self, nums, k):
        if k >= len(nums):
            k = k % len(nums)
        l, r = len(nums) - k - 1, len(nums) - k
        res = [0] * len(nums)
        tmp1 = 0
        tmp2 = len(res) - 1
        while l >= 0 or r < len(nums):
            if l < 0:
                res[tmp1] = nums[r]
                r += 1
                tmp1 += 1
            elif r > len(res) - 1:
                res[tmp2] = nums[l]
                l -= 1
                tmp2 -= 1
            else:
                res[tmp1], res[tmp2] = nums[r], nums[l]
                l -= 1
                r += 1
                tmp1 += 1
                tmp2 -= 1
        for i in range(len(nums)):
            nums[i] = res[i]
a = Solution()
print(a.rotate([1,2], 3))



#############투 포인터 사용 또 다른 케이스###########


class Solution:
    def rotate(self, nums, k):
        def numReverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        k, n = k % len(nums), len(nums)
        if k:
            numReverse(0, n - 1)
            numReverse(0, k - 1)
            numReverse(k, n - 1)
            
            

#############투 포인터 사용 안한 케이스#############


class Solution:
    def rotate(self, nums, k):
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]