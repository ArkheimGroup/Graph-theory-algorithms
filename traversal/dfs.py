# Define the graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = set()           # To track visited nodes
traversal_order = []      # To store DFS traversal result

def dfs(node):
    if node not in visited:
        visited.add(node)                 # Mark node as visited
        traversal_order.append(node)     

        for neighbor in graph[node]:     # Visit all neighbors
            dfs(neighbor)

dfs('A')  # Start DFS from node 'A'
print("DFS Traversal Order:", traversal_order)
