import sys
A, B = list(map(int, sys.stdin.readline().split()))
temp = B
count = 0
while temp > A:
    if temp % 2 == 1:
        temp -= 1
        temp /= 10
    else:
        temp = temp // 2
    count += 1
if temp == A:
    print(count+1)
else:
    print(-1)