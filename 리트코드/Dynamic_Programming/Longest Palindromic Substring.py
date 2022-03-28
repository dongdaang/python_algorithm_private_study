class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        longest_palindrom = s[0]
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
            
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):  
                if s[i] == s[j]:
                    if j - i == 1 or dp[i + 1][j - 1] == 1:
                        dp[i][j] = 1
                        if len(longest_palindrom) < j - i + 1:
                            longest_palindrom = s[i:j + 1]
                
        return longest_palindrom
        
a = Solution()
print(a.longestPalindrome('babad'))