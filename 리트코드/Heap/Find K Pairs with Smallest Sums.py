import heapq

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2: return []
        n, res, cnt, heap = len(nums2), [], 0, [(nums1[i] + nums2[0], i, 0) for i in range(len(nums1))]
        while heap and cnt < k:
            cnt += 1
            sm, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < n: heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return res

a = Solution()
print(a.kSmallestPairs([1,7,11], [2,4,6], 3))


################시간초과 코드...##################
# class Solution:
#     def kSmallestPairs(self, nums1, nums2, k):
#         leftheap = []
#         rightheap = []
#         result = []
#         for i in nums1:
#             for j in nums2:
#                 if len(leftheap) == len(rightheap):
#                     heapq.heappush(leftheap, (i + j, [i, j]))
#                 else:
#                     heapq.heappush(rightheap, (i + j, [i, j]))
#         while len(result) < k:
#             if len(leftheap) == 0 and len(rightheap) == 0:
#                 break
#             elif len(rightheap) == 0:
#                 result.append(heapq.heappop(leftheap)[1])
#             elif len(leftheap) == 0:
#                 result.append(heapq.heappop(rightheap)[1])
#             elif leftheap[0][0] <= rightheap[0][0]:
#                 result.append(heapq.heappop(leftheap)[1])
#             else:
#                 result.append(heapq.heappop(rightheap)[1])
        
#         return result