class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        word = {}
        for i in range(len(pattern)):
            if len(s) != len(pattern):
                return False
            if pattern[i] not in word:
                if s[i] in word.values():
                    return False
                word[pattern[i]] = s[i]
            else:
                if word[pattern[i]] != s[i]:
                    return False
        return True

a = Solution()
print(a.wordPattern("abba", "dog cat cat dog"))