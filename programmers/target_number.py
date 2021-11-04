from collections import deque


def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append([numbers[0], 0]) # 시작점을 위해 queue에 index 0 값을 넣어줌
    queue.append([-numbers[0], 0])
    while queue:
        num, i = queue.popleft()
        if i + 1 == len(numbers): # 먼저 탐색이 완료된 element를 걸러주고(두 if문을 한 줄에 쓰게 되면, 완료된 element가 걸러지지 않고 계속해서 append가 일어남)
            if num == target: # 완료된 element중 target number와 같은 값이 있을 경우
                answer += 1
        else:
            queue.append([num - numbers[i + 1], i + 1])
            queue.append([num + numbers[i + 1], i + 1])
    return answer


print(solution([1, 1, 1, 1, 1], 3))
