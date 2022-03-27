# 연결 요소의 개수
import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())

visited = [False] * (N + 1)
graph = [[] for _ in range(N+1)]
count = 0

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        count += 1
        
print(count)