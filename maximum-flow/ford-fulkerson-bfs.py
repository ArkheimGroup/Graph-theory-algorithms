def ford_fulkerson(graph, source, sink):
    n = len(graph)
    residual = [row[:] for row in graph]

    max_flow = 0

    while True:
        # Unlabel all nodes
        visited = [False] * n

        # Initialize predecessors
        pred = [-1] * n

        # Label source and initialize List
        visited[source] = True
        queue = [source]

        # BFS: Find an augmenting path
        while queue and not visited[sink]:
            u = queue.pop(0)

            for v in range(n):
                if residual[u][v] > 0 and not visited[v]:
                    pred[v] = u
                    visited[v] = True
                    queue.append(v)

        # If sink is unlabeled, no augmenting path exists
        if not visited[sink]:
            break

        # Find the bottleneck capacity
        flow = float('inf') # Positive infinity
        v = sink

        while v != source:
            u = pred[v]
            flow = min(flow, residual[u][v])
            v = u

        # Augment the flow
        v = sink

        while v != source:
            u = pred[v]

            residual[u][v] -= flow
            residual[v][u] += flow

            v = u

        max_flow += flow

    return max_flow


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