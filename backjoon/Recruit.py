import sys
N = int(sys.stdin.readline().rstrip())
for i in range(N):
    count = 1
    ranks = []
    case_count = int(sys.stdin.readline().rstrip())
    for j in range(case_count):
        ranks.append(list(map(int, sys.stdin.readline().rstrip().split())))
    ranks.sort(key=lambda x: x[0])
    min_rank = ranks[0][1]
    for k in range(1, len(ranks)):
        if min_rank > ranks[k][1]:
            count += 1
            min_rank = ranks[k][1]
    print(count)
