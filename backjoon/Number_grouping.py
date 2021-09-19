import sys; r= sys.stdin.readline
N = int(r())


# 짝수 -> 두개씩 묶어서 다 곱함
# 홀수 -> 두개씩 묶어서 곱한 후 마지막 수를 더함
def number_grouping(array):
    length = len(array)
    if length == 0:
        return 0
    else:
        group_result = 0
        if length % 2 == 0:
            for i in range(0, length, 2):
                group_result += array[i] * array[i+1]
        else:
            for i in range(0, length-1, 2):
                group_result += array[i] * array[i+1]
            group_result += array[-1]
        return group_result


positive = []
negative_o = []
result = 0
for i in range(N):
    number = int(r())
    if number < 1:
        negative_o.append(number)
    elif number == 1:
        result += 1
    else:
        positive.append(number)
positive.sort(reverse=True)
negative_o.sort()
result += number_grouping(positive) + number_grouping(negative_o)
print(result)
