import sys
N = int(sys.stdin.readline())
Weights = list(map(int, sys.stdin.readline().rstrip().split()))
Weights.sort()
num = 1
for i in range(N):
    if num < Weights[i]:
        break
    num += Weights[i]
print(num)