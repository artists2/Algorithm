# 미로 탐색
from collections import deque

M, N = map(int, input().split())  # M = x, N = y
maps = []

for _ in range(M):
    maps.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, maps):
    queue = deque()
    queue.append((x, y))

    while queue:

        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
            
    return maps[M-1][N-1]

print(bfs(0, 0, maps))
