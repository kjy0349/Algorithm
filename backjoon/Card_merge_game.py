import sys, heapq
N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
heapq.heapify(cards)
for i in range(M):
    m1 = heapq.heappop(cards)
    m2 = heapq.heappop(cards)
    res = m1 + m2
    heapq.heappush(cards, res)
    heapq.heappush(cards, res)
print(sum(cards))