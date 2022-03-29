# https://leetcode.com/problems/network-delay-time/


import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        def dijkstra(a):
            d[a] = 0
            heapq.heappush(heap, (0, a))
            while heap:
                distance, now = heapq.heappop(heap)
                if d[now] < distance:
                    continue
                for next, weight in connections[now]:
                    nextdistance = d[now] + weight
                    if d[next] > nextdistance:
                        d[next] = nextdistance
                        heapq.heappush(heap, (nextdistance, next))
        
        connections = [[] for _ in range(n + 1)]
        heap = []
        INF = float('inf')
        d = [INF] * (n + 1)
        
        for info in times:
            connections[info[0]].append((info[1], info[2]))
        
        dijkstra(k)
        
        res = max(d[1:])
        if res == INF:
            return -1
        else:
            return res

a = Solution()
print(a.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))