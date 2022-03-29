# https://leetcode.com/problems/open-the-lock/


from collections import deque, defaultdict

class Solution:
    def openLock(self, deadends, target):
        if target == '0000':
            return 0
        if '0000' in deadends:
            return -1
        
        def bfs():
            global cnt
            while queue:
                n = len(queue)
                for _ in range(n):
                    now = queue.popleft()
                    for i in range(4):
                        for j in range(2):
                            nx = str(int(now[i]) + dx[j] + 10)[-1]
                            tmp = now[:i] + nx + now[i + 1:]
                            if tmp in deadends or tmp in visited or tmp == target or tmp in queue:
                                continue
                            if tmp == '0000':
                                return cnt + 1
                            queue.append(tmp)
                cnt += 1
            return -1
                
        queue = deque()
        dx = [-1, 1]
        global cnt
        cnt = 1
        visited = []
        zero_change = defaultdict()
        for i in range(4):
            if target[i] == '0':
                zero_change[i] = ''
        for i in range(4):
            if i in zero_change:
                if target[:i] + '9' + target[i + 1:] not in deadends:
                    zero_change[i] = '-'
                    queue.append(target[:i] + '9' + target[i + 1:])
                    visited.append(target[:i] + '9' + target[i + 1:])
                elif target[:i] + '1' + target[i + 1:] not in deadends:
                    zero_change[i] = '+'
                    queue.append(target[:i] + '1' + target[i + 1:])
                    visited.append(target[:i] + '1' + target[i + 1:])
            else:
                for j in range(2):
                    nx = str(int(target[i]) + dx[j] + 10)[-1]
                    tmp = target[:i] + nx + target[i + 1:]
                    if tmp in deadends or tmp in visited:
                        continue
                    if tmp == '0000':
                        return cnt
                    queue.append(tmp)
                    visited.append(tmp)
        if not queue:
            return -1
        
        return bfs()

a = Solution()
print(a.openLock(["0201","0101","0102","1212","2002"], '0202'))