# 토마토

from collections import deque

N, M = map(int, input().split())

maps = []

for _ in range(M):
    maps.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(maps):
    queue = deque()

    for i in range(M):
        for j in range(N):
            if maps[i][j] == 1:
                queue.append((i, j))

    
    result = []
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if maps[nx][ny] == 1:
                continue
            if maps[nx][ny] == -1:
                continue
            if maps[nx][ny] == 0:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
                result.append(maps[nx][ny])

            if maps[nx][ny] > 1:
                if maps[nx][ny] <= maps[x][y] + 1:
                    continue
                else:
                    maps[nx][ny] = maps[x][y] + 1
                    result.append(maps[nx][ny])


    for i in range(M):
        for j in range(N):
            if maps[i][j] == 0:
                return -1
    if not result:
        return 0
    else:
        return max(result)-1

print(bfs(maps))