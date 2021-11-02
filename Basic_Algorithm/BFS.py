from collections import deque
graph_list = {1: {3, 6, 7},
              2: {6, 5},
              3: {1, 4},
              4: {3},
              5: {2},
              6: {1, 2},
              7: {1, 8},
              8: {7}}
root_node = 1

def BFS_with_adj_list(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited
print(BFS_with_adj_list(graph_list, root_node))