##############투 포인터 사용 안한 풀이############

# class Solution:
#     def moveZeroes(self, nums):
#         for num in nums:
#             if num == 0:
#                 nums.remove(num)
#                 nums.append(0)
#         return nums


###############투 포인터 사용################
class Solution:
    def moveZeroes(self, nums):
        if len(nums) == 1:
            return nums
        else:
            l, r = 0, 1
            while r < len(nums):
                if nums[l] == 0 and nums[r] != 0:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r += 1
                elif nums[l] != 0 and nums[r] != 0:
                    l += 1
                else:
                    r += 1
            return nums
    
a = Solution()
print(a.moveZeroes([0,1,0,3,12]))


###############투 포인터 사용한 다른 솔루션##############


class Solution:
    def moveZeroes(self, nums: list) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            if nums[slow] != 0:
                slow += 1