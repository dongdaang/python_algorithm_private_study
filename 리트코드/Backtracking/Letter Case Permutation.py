class Solution:
    def letterCasePermutation(self, s):
        res = []
        tmp = []
        
        def f(a):
            if len(tmp) == len(s):
                res.append(''.join(tmp[:]))
                return
            for i in range(a, len(s)):
                if s[i].isalpha():
                    if s[i].islower():
                        tmp.append(s[i].upper())
                        f(i + 1)
                        tmp.pop()
                        tmp.append(s[i])
                        f(i + 1)
                        tmp.pop()
                    else:
                        tmp.append(s[i].lower())
                        f(i + 1)
                        tmp.pop()
                        tmp.append(s[i])
                        f(i + 1)
                        tmp.pop()
                else:
                    tmp.append(s[i])
                    f(i + 1)
                    tmp.pop()
        f(0)
        return res

a = Solution()
print(a.letterCasePermutation("3z4"))