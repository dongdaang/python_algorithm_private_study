class Solution:
    def subsets(self, nums):
        res = [[]]
        tmp = []
        
        def backtracking(a):
            for i in range(a, len(nums)):
                tmp.append(nums[i])
                res.append(tmp)
                backtracking(i + 1)
                tmp.pop()
        backtracking(0)
        return res
        
a = Solution()
print(a.subsets([1,2,3]))