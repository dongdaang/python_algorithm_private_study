class Solution:
    def letterCombinations(self, digits):
        if digits == '':
            return []
        def backtracking(a):
            global s
            if len(s) == n:
                if s not in res:
                    res.append(s)
                return
            for c in letters[digits[a]]:
                s += c
                backtracking(a + 1)
                s = s[:-1]
        
        n = len(digits)
        global s
        s = ''
        res = []
        letters = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        backtracking(0)
        
        return res
        
a = Solution()
print(a.letterCombinations('22'))