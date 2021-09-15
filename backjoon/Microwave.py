T = int(input())
times = {300: 0, 60: 0, 10: 0}
time_key = list(times.keys())
compare_counts = [T//time if (T//time) * time == T else 0 for time in time_key]
i = 0
for i in range(len(times)):
    if T // time_key[i] > 0:
        times[time_key[i]] = T // time_key[i]
        T -= T // time_key[i] * time_key[i]

if compare_counts.count(0) == 3:
    if T == 0:
        for value in list(times.values()):
            print(value, end=' ')
    else:
        print(-1)
else:
    if T == 0:
        min_array = min(compare_counts, list(times.values()), key=lambda x: sum(x))
        for value in min_array:
            print(value, end=' ')
    else:
        for value in compare_counts:
            print(value, end=' ')