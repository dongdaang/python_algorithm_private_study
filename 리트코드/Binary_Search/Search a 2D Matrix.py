class Solution:
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        l1, r1 = 0, m - 1
        while l1 <= r1:
            mid1 = (l1 + r1) // 2
            l2, r2 = 0, n - 1
            while l2 <= r2:
                mid2 = (l2 + r2) // 2
                if matrix[mid1][mid2] == target:
                    return True
                elif matrix[mid1][mid2] > target:
                    r2 = mid2 - 1
                else:
                    l2 = mid2 + 1
            if matrix[mid1][r2] > target:
                r1 = mid1 - 1
            else:
                l1 = mid1 + 1
        return False

a = Solution()
print(a.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))





###############다른 솔루션###############


class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        
        while low <= high:
            mid = (low + high) / 2
            num = matrix[mid / cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False