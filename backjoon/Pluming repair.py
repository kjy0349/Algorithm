import sys
N, L = list(map(int, sys.stdin.readline().split()))
Leaks = list(map(int, sys.stdin.readline().split()))
finish = 0
count = 0
Leaks.sort()

for leak in Leaks:
    if finish <= leak - 0.5:
        finish = leak - 0.5 + L
        count += 1
    else:
        pass
print(count)