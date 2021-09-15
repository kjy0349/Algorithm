import sys
N = int(sys.stdin.readline().rstrip())
ropes = []
for i in range(N):
    ropes.append(int(sys.stdin.readline().rstrip()))
ropes.sort(reverse=True)
for i in range(len(ropes)):
    ropes[i] = (i+1) * ropes[i]
print(max(ropes))