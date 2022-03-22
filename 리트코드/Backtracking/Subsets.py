class Solution:
    def subsets(self, nums):
        res = [[]]
        tmp = []

        def f(a):
            for i in range(a, len(nums)):
                tmp.append(nums[i])
                res.append(tmp[:])
                f(i + 1)
                tmp.pop()
        
        f(0)
        return res


    
###############솔루션################

class Solution:
    def subsets(self, nums):
        nums.sort()
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
        return result
    
a = Solution()
print(a.subsets([1,2,3]))