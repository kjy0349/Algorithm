import sys; r = sys.stdin.readline
i = 1
while True:
    L, P, V = list(map(int, r().rstrip().split()))
    if L == 0 and P == 0 and V == 0:
        break
    last = V // P
    print("Case %d: %d" %(i, last * L + min(V % P, L)))
    i += 1