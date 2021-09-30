import sys
import heapq
N = int(sys.stdin.readline())
lectures = []
rooms = []
count = 1
for i in range(N):
    heapq.heappush(lectures, (list(map(int, sys.stdin.readline().rstrip().split()))))
heapq.heappush(rooms, heapq.heappop(lectures)[1])
for i in range(N-1):
    end_time = heapq.heappop(rooms)
    new_lecture = heapq.heappop(lectures)
    if end_time > new_lecture[0]:
        count += 1
        heapq.heappush(rooms, end_time)
        heapq.heappush(rooms, new_lecture[1])
    else:
        heapq.heappush(rooms, new_lecture[1])
print(count)
