# 정답 코드
import sys

N, K = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().strip()))

result = []
delNum = K

for i in range(N):
    while delNum > 0 and result:
        if result[len(result) - 1] < nums[i]:
            result.pop()
            delNum -= 1
        else:
            break
    result.append(nums[i])

for i in range(N - K):
    print(result[i], end="")

# 틀린 코드
import sys

N, K = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().strip()))
result = []
for i in range(N):
    while result and K > 0:
        if result[-1] < numbers[i]:
            result.pop()
            K -= 1
        else:
            break
    result.append(numbers[i])
print(''.join(list(map(str, result))))
