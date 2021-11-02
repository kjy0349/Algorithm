import itertools
def solution(numbers, target):
    minus_numbers = [-num for num in numbers]
    possibles = list(itertools.product(numbers, minus_numbers))
    print(possibles)
    s_p = list(map(sum, possibles))
    return s_p.count(target)
print(solution([1, 1, 1, 1, 1], 3))