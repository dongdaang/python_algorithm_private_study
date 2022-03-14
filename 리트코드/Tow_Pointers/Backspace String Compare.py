class Solution:
    def backspaceCompare(self, s, t):
        letters1 = []
        letters2 = []
        for i in range(len(s)):
            if s[i] == '#':
                if letters1:
                    letters1.pop()
            else:
                letters1.append(s[i])
        for i in range(len(t)):
            if t[i] == '#':
                if letters2:
                    letters2.pop()
            else:
                letters2.append(t[i])
        if letters1 == letters2:
            return True
        else:
            return False
a = Solution()
print(a.backspaceCompare("a#c", "b"))




##############투포인터 활용##################


class Solution:
    def backspaceCompare(self, S, T):
        si, ti = len(S) - 1, len(T) - 1
        count_s = count_t = 0
        
        while si >= 0 or ti >= 0:
            while si >= 0:
                if S[si] == '#':
                    count_s += 1
                    si -= 1
                elif S[si] != '#' and count_s > 0:
                    count_s -= 1
                    si -= 1
                else:
                    break

            while ti >= 0:
                if T[ti] == '#':
                    count_t += 1
                    ti -= 1
                elif T[ti] != '#' and count_t > 0:
                    count_t -= 1
                    ti -= 1
                else:
                    break
            
            
            if (ti < 0 and si >= 0) or (si < 0 and ti >= 0):
                return False
            if (ti >= 0 and si >= 0) and S[si] != T[ti]:
                return False
            
            si -= 1
            ti -= 1
        return True