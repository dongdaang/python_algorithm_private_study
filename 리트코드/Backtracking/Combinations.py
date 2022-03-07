class Solution:
    def combine(self, n, k):
        res = []
        tmp = []
        
        def f(a):
            if len(tmp) == k:
                res.append(tmp[:])
                return
            for i in range(a, n + 1):
                if i not in tmp:
                    tmp.append(i)
                    f(i + 1)
                    tmp.pop()
        f(1)
        return res

a = Solution()
print(a.combine(4, 2))