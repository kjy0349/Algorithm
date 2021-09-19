import sys

r = sys.stdin.readline
P = []
Q = []
N, M = list(map(int, r().split()))
for i in range(N):
    P.append(list(map(int, list(r().rstrip()))))
for i in range(N):
    Q.append(list(map(int, list(r().rstrip()))))


def matrix(A, B):
    count = 0
    if A == B:
        return 0
    else:
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] != B[i][j]:
                    if i + 2 < len(A) and j + 2 < len(A[i]):
                        count += 1
                        for k in range(i, i + 3):
                            for m in range(j, j + 3):
                                A[k][m] = 1 - A[k][m]
    if A == B:
        return count
    else:
        return -1


print(matrix(P, Q))
