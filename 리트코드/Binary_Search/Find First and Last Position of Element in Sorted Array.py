class Solution:
    def searchRange(self, nums, target):
        res = []
        ans = []
        def binary_search(start, end):
            if start > end:
                return
            mid = (start + end) // 2
            if nums[mid] == target:
                res.append(mid)
                binary_search(start, mid - 1)
                binary_search(mid + 1, end)
            elif nums[mid] > target:
                binary_search(start, mid - 1)
            else:
                binary_search(mid + 1, end)
                    
        binary_search(0, len(nums) - 1)
        if len(res) == 0:
            ans = [-1, -1]
        elif len(res) == 1:
            ans = [res[0], res[0]]
        else:
            ans = [min(res), max(res)]
        
        return ans

a = Solution()
print(a.searchRange([5,7,7,8,8,10], 8))



###############다른 솔루션#################

class Solution:
    def searchRange(self, nums, target):
        def search(n):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] >= n:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        lo = search(target)
        return [lo, search(target+1)-1] if target in nums[lo:lo+1] else [-1, -1]