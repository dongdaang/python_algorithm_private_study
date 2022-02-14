##############느린 코드##############

# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         if sum(nums[1:]) == 0:
#             return 0
#         for i in range(1, len(nums)):
#             if sum(nums[:i]) == sum(nums[i+1:]):
#                 return i
#         if sum(nums[:-1]) == 0:
#             return 0
#         return -1

##############더 빠른 코드#############
class Solution(object):
    def pivotIndex(self, nums):
        # Time: O(n)
        # Space: O(1)
        left, right = 0, sum(nums)
        for index, num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        return -1