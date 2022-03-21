class Solution:
    def allPathsSourceTarget(self, graph):
        def dfs(i):
            road.append(i)
            if i == n - 1:
                res.append(road[:])
                return
            for j in graph[i]:
                if j in road:
                    continue
                dfs(j)
                road.pop()
        
        n = len(graph)
        res = []
        road = []
        dfs(0)
        
        return res
        
a = Solution()
print(a.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))