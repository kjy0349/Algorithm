def solution(v):
    answer = []
    numbers_x = {}
    numbers_y = {}
    for x, y in v:
        if x not in numbers_x:
            numbers_x[x] = 1
        else:
            numbers_x[x] += 1
        if y not in numbers_y:
            numbers_y[y] = 1
        else:
            numbers_y[y] += 1
    for num in list(numbers_x.keys()):
        if numbers_x[num] != 2:
            answer.append(num)
    for num in list(numbers_y.keys()):
        if numbers_y[num] != 2:
            answer.append(num)
    return answer
print(solution([[1, 4], [3, 4], [3, 10]]))