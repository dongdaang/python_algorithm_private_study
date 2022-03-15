from collections import Counter, defaultdict

class Solution:
    def findAnagrams(self, s, p):
        letters = Counter(p)
        now = 0
        res = []
        for i in range(len(s) - len(p) + 1):
            if Counter(s[i:i + len(p)]) == letters:
                res.append(i)
        return res
a = Solution()
print(a.findAnagrams("cbaebabacd", "abc"))



##############슬라이드 윈도우 활용 솔루션##############

class Solution:
    def findAnagrams(self, s, p):
        hm, res, pL, sL = defaultdict(int), [], len(p), len(s)
        if pL > sL: return []

        # build hashmap
        for ch in p: hm[ch] += 1

        # initial full pass over the window
        for i in range(pL-1):
            if s[i] in hm: hm[s[i]] -= 1
            
        # slide the window with stride 1
        for i in range(-1, sL-pL+1):
            if i > -1 and s[i] in hm:
                hm[s[i]] += 1
            if i+pL < sL and s[i+pL] in hm: 
                hm[s[i+pL]] -= 1
                
            # check whether we encountered an anagram
            if all(v == 0 for v in hm.values()): 
                res.append(i+1)
                
        return res