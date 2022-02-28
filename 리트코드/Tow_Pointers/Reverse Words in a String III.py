class Solution:
    def reverseWords(self, s):
        words = s.split(' ')
        res = ''
        for word in words:
            _word = list(word)
            l, r = 0, len(_word) - 1
            while l <= r:
                _word[l], _word[r] = _word[r], _word[l]
                l += 1
                r -= 1
            res += ''.join(_word) + ' '
        return res[:-1]

a = Solution()
print(a.reverseWords("Let's take LeetCode contest"))



#############다른 솔루션############


class Solution:
    def reverseWords(self, s: str) -> str:
        split_list = s.split(" ")
        split_list = [i[::-1] for i in split_list]
        return " ".join(split_list)