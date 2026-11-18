from collections import deque

def topoSort(adj):
    n = len(adj)
    indegree = [0] * n
    res = []
    queue = deque()

    # Compute indegrees
    for i in range(n):
        for next_node in adj[i]:
            indegree[next_node] += 1
            
    # Add all nodes with indegree 0 
    # into the queue
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)

    # Kahn’s Algorithm
    while queue:
        top = queue.popleft()
        res.append(top)
        for next_node in adj[top]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                queue.append(next_node)

    return res

def addEdge(adj, u, v):
    adj[u].append(v)

# Example
n = 6
adj = [[] for _ in range(n)]

addEdge(adj, 0, 1)
addEdge(adj, 1, 2)
addEdge(adj, 2, 3)
addEdge(adj, 4, 5)
addEdge(adj, 5, 1)
addEdge(adj, 5, 2)

res = topoSort(adj)
print(*res)