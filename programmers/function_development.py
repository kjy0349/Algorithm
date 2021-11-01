from collections import deque
def solution(progresses, speeds):
    pro_deque = deque()
    pro_deque.extend(progresses)
    speed_deque = deque()
    speed_deque.extend(speeds)
    answer = []
    while len(pro_deque) > 1:
        for i in range(len(pro_deque)):
            pro_deque[i] += speed_deque[i]
        temps = []
        while pro_deque[0] >= 100:
            temps.append(pro_deque.popleft())
            speed_deque.popleft()
            if len(pro_deque) == 0:
                break
        if temps:
            answer.append(len(temps))
    if pro_deque:
        answer.append(1)
    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))