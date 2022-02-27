##############투 포인터 안쓴거#############

# class Solution:
#     def sortedSquares(self, nums):
#         new_nums = [num ** 2 for num in nums]
#         new_nums.sort()
#         return new_nums

# a = Solution()
# print(a.sortedSquares([-4,-1,0,3,10]))



##############투 포인터##############


class Solution:
    def sortedSquares(self, nums):
        start = 0
        end = len(nums) - 1
        res = [0] * len(nums)
        while start <= end:
            if abs(nums[start]) > abs(nums[end]):
                res[end - start] = (nums[start] ** 2)
                start += 1
            else:
                res[end - start] = (nums[end] ** 2)
                end -= 1
        return res

a = Solution()
print(a.sortedSquares([-4,-1,0,3,10]))