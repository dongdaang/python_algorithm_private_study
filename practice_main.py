def solution(info, edges):
    answer = tree(0, 0, info, edges)
    return answer
def tree(pos, tmp):
    sheeps = 1
    wolves = 0
    for node in edges:
        if node[0] == pos:
            if info[node[1]] == 0:
                sheeps += 1
                pos = node[1]
                tmp = node[1]
                tree(pos, tmp)
            else:
                if wolves + 1 < sheeps:
                    wolves += 1
                    pos = node[1]
                    tmp = node[1]
                    tree(pos, tmp)
                else:
                    pos = tmp
    return sheeps