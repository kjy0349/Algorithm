import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        scovil = heapq.heappop(scoville)
        if scovil >= K:
            break
        elif len(scoville) == 0:
            return -1
        else:
            heapq.heappush(scoville, scovil + (heapq.heappop(scoville) * 2))
            answer += 1
    return answer
print(solution([1, 2, 3], 13))