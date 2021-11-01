import itertools
def is_prime(num):
    if num < 2:
        return False
    else:
        is_pri = True
        for i in range(2, num//2 + 1):
            if num % i == 0:
                is_pri = False
                break
            else:
                pass
        return is_pri

def solution(numbers):
    answer = 0
    possibles = []
    poss_dict = {}
    for i in range(1, len(numbers)+1):
        possibles.append(list(map(int, map("".join, itertools.permutations(numbers, i)))))
    for i in range(len(possibles)):
        for j in range(len(possibles[i])):
            poss_dict[possibles[i][j]] = 0

    for num in list(poss_dict.keys()):
        if is_prime(num):
            answer += 1
    return answer
print(solution('17'))
