class Solution:
    def permuteUnique(self, nums):
        res = []
        tmp = []
        n = len(nums)
        
        def f():
            if len(tmp) == n:
                a = list(nums[i] for i in tmp)
                if a not in res:
                    res.append(a)
                return
            for i in range(n):
                if i in tmp:
                    continue
                tmp.append(i)
                f()
                tmp.pop()
        f()
        return res

a = Solution()
print(a.permuteUnique([1,2,3]))