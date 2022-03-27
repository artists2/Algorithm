# 안전 영역
import sys
sys.setrecursionlimit(10000000)

N = int(input())

graph = []
visited = [[False] * N for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

depth = set()

for g in graph:
    depth.update(set(g))

def dfs(x, y, d):
    visited[x][y] == True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= N or ny >= N or nx < 0 or ny < 0:
            continue
        else:
            if graph[nx][ny] > d:
                dfs(nx, ny, d)
            else:
                continue
    return

max_count = []
count = 0

for d in depth:
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                dfs(i, j, d)
                count += 1
                pass
    max_count.append(max(max_count, count))
print(max_count)
