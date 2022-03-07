class Solution:
    def permute(self, nums):
        res = []
        tmp = []
        
        def f():
            if len(tmp) == len(nums):
                res.append(tmp[:])
                return
            for i in nums:
                if i in tmp:
                    continue
                tmp.append(i)
                f()
                tmp.pop()
        f()
        return res

a = Solution()
print(a.permute([1, 2, 3]))