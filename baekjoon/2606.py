# 바이러스


def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

computers = int(input())
networks = int(input())

visited = [False] * (computers + 1)
graph = [[] for _ in range(computers + 1)]

for _ in range(networks):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# for i in range(1, computers+1):
#     graph[i].sort()

dfs(graph, 1, visited)

print(visited.count(True)-1)



