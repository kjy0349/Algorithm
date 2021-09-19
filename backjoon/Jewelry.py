import sys; r = sys.stdin.readline
N, K = list(map(int, r().rstrip().split()))
jewelry = []
result = 0
for i in range(N):
    jewelry.append(list(map(int, r().rstrip().split())))
weights = []
for i in range(K):
    weights.append(int(r()))
weights.sort(reverse=True)
jewelry.sort(key= lambda x: x[1], reverse=True)
for i in range(len(jewelry)):
    if len(weights) == 0:
        break
    for j in range(len(weights)):
        if jewelry[i][0] < weights[j]:
            result += jewelry[i][1]
            del jewelry[i], weights[j]
print(result)
