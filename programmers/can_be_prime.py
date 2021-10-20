def is_prime(number):
    is_prime = True
    for i in range(number//2, number):
        if number % i == 0:
            is_prime = False
            break
    return is_prime

def solution(numbers):
    answer = 0
    numbers_convert = list(numbers)
    for num in numbers_convert:
        if is_prime(num):
            answer += 1
    for i in range(len(numbers_convert)):
        max_length = i + 1
        numbers_c = numbers_convert
        number = ""
        for j in range()




    return answer

# 7자리일경우
# 1개씩 고르는 경우의 수 : nP1
# 2개씩 고르는 경우의 수 : nP2
# 3개씩 고르는 경우의 수 : nP3
# .... : nPn