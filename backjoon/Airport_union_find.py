import sys
G = int(sys.stdin.readline())
P = int(sys.stdin.readline())
pLists = [int(sys.stdin.readline()) for _ in range(P)]
def find_parent(x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    parent[x] = y

parent = {i:i for i in range(G+1)}
count = 0
for plane in pLists:
    p = find_parent(plane)
    if p == 0:
        break
    union(p, p-1)
    count += 1
print(count)
