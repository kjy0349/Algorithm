from collections import deque
graph_list = {1: {3, 4},
              2: {3, 4, 5},
              3: {1, 5},
              4: {1},
              5: {2, 6},
              6: {3, 5}}
root_node = 1
print(graph_list)
def DFS_with_adj_list(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited
print(DFS_with_adj_list(graph_list, 1))
