def solution(n, lost, reserve):
    i = 0
    while i < len(lost):
        if lost[i] in reserve:
            reserve.remove(lost[i])
            lost.remove(lost[i])
            i -= 1
        i += 1
    i = 0
    lost.sort()
    reserve.sort()
    while i < len(lost):
        steal = lost[i]
        if steal - 1 in reserve:
            reserve.remove(steal - 1)
            lost.remove(steal)
            i -= 1
        elif steal + 1 in reserve:
            reserve.remove(steal + 1)
            lost.remove(steal)
            i -= 1
        i += 1
    if lost:
        n -= len(lost)
    return n
print(solution(4, [4, 2], [3, 5]))