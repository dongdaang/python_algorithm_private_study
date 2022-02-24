class Solution:
    def isValid(self, s):
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if (i == ')' and stack.pop() != '(') or (i == '}' and stack.pop() != '{') or (i == ']' and stack.pop() != '['):
                    return False
        if len(stack) != 0:
            return False
        return True
        
a = Solution()
print(a.isValid("()"))



##########딕셔너리 활용 솔루션##########


# class Solution:
#     # @return a boolean
#     def isValid(self, s):
#         stack = []
#         dict = {"]":"[", "}":"{", ")":"("}
#         for char in s:
#             if char in dict.values():
#                 stack.append(char)
#             elif char in dict.keys():
#                 if stack == [] or dict[char] != stack.pop():
#                     return False
#             else:
#                 return False
#         return True