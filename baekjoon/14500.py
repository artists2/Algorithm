# 테트로미노
import sys

N, M = map(int, input().split())

maps = []

for _ in range(N):
    maps.append(list(map(int, sys.stdin.readline().split())))
    
visited = [[0] * M for _ in range(N)]

result = 0

dx = [-1, 0, 1, 0]  # [1, -1, 0, 0]
dy = [0, 1, 0, -1]  # [0, 0, 1, -1]

max_val = max(map(max, maps))

def dfs(x, y, c, v):
    global result

    if result >= v + max_val * (4 - c):
        return

    if c == 4:
        result = max(v, result)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 0:
                if c == 2:
                    visited[nx][ny] = 1
                    dfs(x, y, c+1, v + maps[nx][ny])
                    visited[nx][ny] = 0

                visited[nx][ny] = 1
                dfs(nx, ny, c+1, v + maps[nx][ny])
                visited[nx][ny] = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 1, maps[i][j])
        visited[i][j] = 0

print(result)
