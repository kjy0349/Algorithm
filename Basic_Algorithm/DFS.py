graph_list = {1: {3, 6, 7},
              2: {6, 5},
              3: {1, 4},
              4: {3},
              5: {2},
              6: {1, 2},
              7: {1, 8},
              8: {7}}
root_node = 1
def DFS_with_adj_list(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited
print(DFS_with_adj_list(graph_list, root_node))
