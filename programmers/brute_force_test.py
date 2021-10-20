def solution(answers):
    pattern_one = [1, 2, 3, 4, 5]
    pattern_two = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern_three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    patterns = []
    patterns.append(pattern_one)
    patterns.append(pattern_two)
    patterns.append(pattern_three)
    answer_count = [0, 0, 0]
    for i in range(3):
        j = 0
        for ans in answers:
            if j == len(patterns[i]):
                j = 0
            if ans == patterns[i][j]:
                answer_count[i] += 1
            else:
                pass
            j += 1
    first_st = max(answer_count)
    result = []
    if answer_count.count(first_st) > 1:
        for i in range(len(answer_count)):
            if first_st == answer_count[i]:
                result.append(i+1)
        return result
    else:
        return [answer_count.index(first_st) + 1]