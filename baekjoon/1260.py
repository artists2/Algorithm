# DFS와 BFS
from collections import deque


def dfs(graph, v, visited):
    print(v, end=' ')
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    visited[v] = True
    queue = deque([v])

    while queue:
        element = queue.popleft()
        print(element, end=' ')

        for i in graph[element]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True



N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, N+1):
    graph[i].sort()

dfs(graph, V, visited)
print()
visited = [False] * (N+1)
bfs(graph, V, visited)
print()

# dfs(V)