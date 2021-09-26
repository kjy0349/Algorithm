import sys
N = int(sys.stdin.readline())
lectures = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
lectures.sort(key=lambda x: x[0])
count = 0
allocated = []
is_allocated = False
for lecture in lectures:
    for i, room in enumerate(allocated):
        if lecture[0] >= room:
            allocated[i] = lecture[1]
            is_allocated = True
            break
    if is_allocated:
        is_allocated = False
        pass
    else:
        allocated.append(lecture[1])
        count += 1
print(count)
