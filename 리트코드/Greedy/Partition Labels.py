class Solution:
    def partitionLabels(self, s):
        letters = [s[0]]
        res = []
        pos = 0
        
        for i in range(1, len(s)):
            if s[i] not in letters:
                tmp = 0
                for letter in letters:
                    if letter in s[i+1:]:
                        break
                    tmp += 1
                if tmp == len(letters):
                    res.append(i - pos)
                    pos = i
                    letters = [s[pos]]
                letters.append(s[i])
        res.append(len(s) - pos)
        return res
    
a = Solution()
print(a.partitionLabels("eccbbbbdec"))



###############다른 솔루션##############


# def partition_labels(S):
    
# 	rightmost = {c:i for i, c in enumerate(S)}
# 	left, right = 0, 0

# 	result = []
# 	for i, letter in enumerate(S):

# 		right = max(right,rightmost[letter])
	
# 		if i == right:
# 			result += [right-left + 1]
# 			left = i+1

# 	return result