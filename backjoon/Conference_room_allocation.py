N = int(input())
times = []
for i in range(N):
    times.append(list(map(int, input().split())))
conference_count = 0
count = 0
times.sort(key=lambda x: (x[1], x[0]))
for start_time, fin_time in times:
    if start_time >= count:
        count = fin_time
        conference_count += 1
    else:
        pass
print(conference_count)