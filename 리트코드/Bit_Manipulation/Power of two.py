class Solution:
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        num = bin(n)
        for i in range(3, len(num)):
            if num[i] == '1':
                return False
        return True

a = Solution()
print(a.isPowerOfTwo(16))


########&연산자 사용#########
class Solution(object):
    def isPowerOfTwo(self, n):
        return n and not (n & n - 1)