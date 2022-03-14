class Solution:
    def intervalIntersection(self, firstList, secondList):
        i, j = 0, 0
        res = []
        while i < len(firstList) and j < len(secondList):
            if firstList[i][0] <= secondList[j][0] <= firstList[i][1]:
                if secondList[j][1] <= firstList[i][1]:
                    res.append(secondList[j])
                    j += 1
                else:
                    res.append([secondList[j][0], firstList[i][1]])
                    i += 1
            elif secondList[j][0] <= firstList[i][0] <= secondList[j][1]:
                if firstList[i][1] <= secondList[j][1]:
                    res.append(firstList[i])
                    i += 1
                else:
                    res.append([firstList[i][0], secondList[j][1]])
                    j += 1
            elif secondList[j][1] < firstList[i][0]:
                j += 1
            elif firstList[i][1] < secondList[j][0]:
                i += 1
        return res
        
a = Solution()
print(a.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))