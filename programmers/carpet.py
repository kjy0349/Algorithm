import math


def solution(brown, yellow):
    answer = []
    y_width, y_height = 0, 0
    y_round = (brown - 4) // 2
    sqrt_num = int(math.sqrt(yellow))
    for i in range(sqrt_num, 0, -1):
        if i + yellow // i == y_round:
            y_width = yellow // i
            y_height = i
            break
    answer.append(y_width + 2)
    answer.append(y_height + 2)
    return answer

print(solution(24, 24))