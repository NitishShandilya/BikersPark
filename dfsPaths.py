"""
Given a graph with or without cycles, a source vertex s and a destination vertex d,
print all paths from given s to d.
The algorithm follows DFS or Depth first search strategy
"""
def all_paths_dfs(graph, start, goal):
    queue = [(start, [start])]
    visited = {}
    visited[start] = True
    paths = []
    while queue:
        (vertex, path) = queue.pop()
        nodes = graph[vertex]
        for i in range(len(nodes)):
            next_node = nodes[i]
            if next_node not in visited or visited[next_node] is False:
                visited[next_node] = True
                if next_node == goal:
                    paths.append(path + [next_node])
                    visited[next_node] = False # Since we want all paths to this node
                else:
                    queue.append((next_node, path + [next_node]))

    return paths

# Test
graph = {'A': ['A','B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}
print all_paths_dfs(graph, 'C', 'F')