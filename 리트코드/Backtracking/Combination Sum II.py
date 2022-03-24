class Solution:
    def combinationSum2(self, candidates, target):
        def dfs(nums, target, index, tmp, res):
            if target < 0:
                return
            elif target == 0:
                res.append(tmp)
                return
            for i in range(index, len(nums)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                dfs(nums, target - nums[i], i + 1, tmp + [nums[i]], res)
        
        res = []
        candidates.sort()
        dfs(candidates, target, 0, [], res)
        return res
        
a = Solution()
print(a.combinationSum2([10,1,2,7,6,1,5], 8))