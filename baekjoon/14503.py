# 로봇 청소기
from sys import stdin


N, M = map(int, input().split())
r, c, d = map(int, input().split())
result = 0
maps = []
dx = [-1, 0, 1, 0]  # [-1, 0, 1, 0] 
dy = [0, 1, 0, -1]  # [0, 1, 0, -1] 

for _ in range(N):
    maps.append(list(map(int, stdin.readline().split())))

def turn_left(d: int) -> int:
    return (d - 1) % 4

def turn_back(d: int) -> int:
    return (d + 2) % 4

def cleaner(x, y, d):
    global result
    if maps[x][y] == 0:
        maps[x][y] = 2
        result += 1
    for _ in range(4):
        nd = turn_left(d)
        nx = x + dx[nd]
        ny = y + dy[nd]

        if maps[nx][ny] == 0:
            cleaner(nx, ny, nd)
            return
        d = nd
    nd = turn_back(d)
    nx = x + dx[nd]
    ny = y + dy[nd]
    if maps[nx][ny] == 1:
        return
    cleaner(nx, ny, d)

cleaner(r, c, d)
print(result)

