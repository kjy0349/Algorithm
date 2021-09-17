import heapq
import sys; r=sys.stdin.readline
N = int(r())
card_counts = []
result = 0
for i in range(N):
    heapq.heappush(card_counts, int(r()))

card_counts.sort()
while len(card_counts) > 1:
    f_operand = heapq.heappop(card_counts)
    s_operand = heapq.heappop(card_counts)
    sub_sum = f_operand + s_operand
    result += sub_sum
    heapq.heappush(card_counts, sub_sum)
    print(card_counts)
print(result)