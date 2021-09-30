import sys
R, C = map(int, sys.stdin.readline().rstrip().split())
def solve(i, j):
    if j == C-1: # 끝 점에 도착
        return True
    for d in dx:
        if 0 <= i + d < R and table[i+d][j+1] == '.' and not visit[i+d][j+1]:
            # 첫번째 조건 : 다음줄이 마지막줄 일때 까지만
            # 두번째 조건 : 나아갈 공간이 빌딩이 없는 갈 수 있는 곳일 때
            # 세번째 조건 : 방몬한적이 없는 곳일 때
            visit[i+d][j+1] = True
            if solve(i+d, j+1):
                return True
    return False
table = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
visit = [[False] * C for _ in range(R)]
dx = [-1, 0, 1]
count = 0
for i in range(R):
    if table[i][0] == '.':
        if solve(i,0):
            count += 1
print(count)