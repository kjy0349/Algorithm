def solution(n, computers):
    answer = 0
    visited = []
    possibles = [i for i in range(n)]
    stack = [0]
    while stack:
        sp = stack.pop()
        if sp not in visited:
            visited.append(sp)
            temp = []
            for i, num in enumerate(computers[sp]):
                if num == 1:
                    temp.append(i)
                else:
                    pass
            stack += set(temp) - set(visited)
        if len(visited) < n and not stack:
            answer += 1
            for num in possibles:
                if num not in visited:
                    stack += [num]
                    break
                else:
                    pass
    return answer + 1
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))