class Solution:
    def subsetsWithDup(self, nums):
        res = [[]]
        tmp = []
        nums.sort()
        
        def f(a):
            for i in range(a ,len(nums)):
                tmp.append(nums[i])
                if tmp not in res:
                    res.append(tmp[:])
                f(i + 1)
                tmp.pop()
        f(0)
        
        return res

a = Solution()
print(a.subsetsWithDup([4,4,4,1,4]))