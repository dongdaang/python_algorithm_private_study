import heapq

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        info = []
        tmp = []
        for i in nums1:
            for j in nums2:
                heapq.heappush(info, ([i, j], i + j))
        for i in info[:k]:
            tmp.append(i[0])
        return tmp

a = Solution()
print(a.kSmallestPairs([1,2,4,5,6], [3,5,7,9], 3))