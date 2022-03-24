from collections import Counter

class Solution:
    def combinationSum(self, candidates, target):
        res = []
        tmp = []
        candidates.sort()
        def backtracking(a):
            if sum(tmp) == target:
                flag = True
                for x in res:
                    if Counter(x) == Counter(tmp):
                        flag = False
                        break
                if flag:
                    res.append(tmp[:])
                return
            for i in range(a, len(candidates)):
                if sum(tmp) + candidates[i] > target:
                    break
                tmp.append(candidates[i])
                backtracking(a)
                tmp.pop()
                
        backtracking(0)
        
        return res

a = Solution()
print(a.combinationSum([2,3,6,7], 7))



################솔루션#################

def combinationSum(self, candidates, target):
    res = []
    candidates.sort()
    self.dfs(candidates, target, 0, [], res)
    return res
    
def dfs(self, nums, target, index, path, res):
    if target < 0:
        return  # backtracking
    if target == 0:
        res.append(path)
        return 
    for i in range(index, len(nums)):
        self.dfs(nums, target-nums[i], i, path+[nums[i]], res)