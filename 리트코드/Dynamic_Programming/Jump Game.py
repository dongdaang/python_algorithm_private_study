class Solution:
    def canJump(self, nums):
        n = len(nums)
        if n == 1:
            return True
        visited = [False] * n
        visited[0] = True
        for i in range(n):
            if visited[i] == False:
                return False
            for j in range(i + 1, i + 1 + nums[i]):
                if visited[j] == True:
                    continue
                visited[j] = True
                if visited[-1] == True:
                    return True
                
a = Solution()
print(a.canJump([3,2,1,0,4]))



#############솔루션#############


def canJump(self, nums):
    m = 0
    for i, n in enumerate(nums):
        if i > m:
            return False
        m = max(m, i+n)
    return True