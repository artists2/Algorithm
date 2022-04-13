# 벽 부수고 이동하기
import sys
from collections import deque
from termios import VSUSP

input = sys.stdin.readline

N, M = map(int, input().split())
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
graph = []
result = []

for _ in range(N):
    graph.append(list(map(int, input()[:-1])))

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

def bfs(r, c, w):
    q = deque()
    q.append((r, c, w))
    visited[0][0][0] = 1

    while q:
        r, c, w = q.popleft()
        
        if r == N-1 and c == M-1:
            return visited[N-1][M-1][w]
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                continue

            if graph[nr][nc] == 0 and visited[nr][nc][w] == 0:
                visited[nr][nc][w] = visited[r][c][w] + 1
                q.append((nr, nc, w))

            if graph[nr][nc] == 1 and w == 0:
                visited[nr][nc][w + 1] = visited[r][c][w] + 1
                q.append((nr, nc, w + 1))
    return -1

print(bfs(0, 0, 0))

for v in visited:
    print(v)