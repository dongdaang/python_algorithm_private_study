from collections import deque

class Solution:
    def brokenCalc(self, startValue, target):
        def bfs():
            while queue:
                now = queue.popleft()
                if now == target:
                    return d[now]
                point1 = now * 2
                point2 = now - 1
                if now > target:
                    d[point2] = min(d[point2], d[now] + 1)
                    queue.append(point2)
                else:
                    d[point1] = min(d[point1], d[now] + 1)
                    d[point2] = min(d[point2], d[now] + 1)
                    queue.append(point1)
                    queue.append(point2)
        
        d = [100] * 100
        d[startValue] = 0
        queue = deque([startValue])
        
        return bfs()
        
a = Solution()
print(a.brokenCalc(3, 10))