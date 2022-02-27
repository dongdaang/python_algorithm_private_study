class Solution:
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1
        while True:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1

a = Solution()
print(a.twoSum([2,7,11,15], 9))