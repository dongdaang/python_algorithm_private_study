class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best_len = 0
        found_set = set()
        l = 0
        r = 0

        for r in range(len(s)):
            while s[r] in found_set:
                found_set.remove(s[l])
                l += 1

            best_len = max(best_len, r-l+1)
            found_set.add(s[r])

        return best_len

a = Solution()
print(a.lengthOfLongestSubstring("abcabcbb"))