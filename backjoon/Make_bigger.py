import sys, heapq
N, K = list(map(int, sys.stdin.readline().split()))
num = sys.stdin.readline().rstrip()
Number = {}
max_num, max_index = 0, 0
for i in range(N):
    if int(num[i]) > max_num:
        max_num = int(num[i])
        max_index = i
    Number[i] = int(num[i])
if max_index > 0:
    min_heap = []
    for i in range(max_index):
        heapq.heappush(min_heap, (Number[i], i))
    if len(min_heap) > K:
        for i in range(K):
            del Number[heapq.heappop(min_heap)[1]]
    else:
        K = K - len(min_heap)
        for i in range(len(min_heap)):
            del Number[heapq.heappop(min_heap)[1]]
        for i in range(max_index, len(Number)):
            heapq.heappush(min_heap, (Number[i], i))
        while K > 0:
            del Number[heapq.heappop(min_heap)[1]]
            K -= 1
else:
    min_heap = []
    for i in range(len(Number)):
        heapq.heappush(min_heap, (Number[i], i))
    for i in range(K):
        del Number[heapq.heappop(min_heap)[1]]
result = list(map(str,Number.values()))
print(''.join(result))