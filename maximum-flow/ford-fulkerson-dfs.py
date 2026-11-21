
from collections import defaultdict

def ford_fulkerson(graph, source, sink):
    n = len(graph)
    residual = [row[:] for row in graph]

    def dfs(u, visited, flow):
        if u == sink:
            return flow

        visited[u] = True

        for v in range(n):
            if not visited[v] and residual[u][v] > 0:
                pushed = dfs(
                    v,
                    visited,
                    min(flow, residual[u][v])
                )

                if pushed > 0:
                    residual[u][v] -= pushed
                    residual[v][u] += pushed
                    return pushed

        return 0

    max_flow = 0

    while True:
        visited = [False] * n
        pushed = dfs(source, visited, float('inf'))

        if pushed == 0:
            break

        max_flow += pushed

    return max_flow


# Example graph (adjacency matrix)
graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]
]

source = 0
sink = 5

print(ford_fulkerson(graph, source, sink))
