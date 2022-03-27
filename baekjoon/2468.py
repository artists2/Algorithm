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
    
    if graph[x][y] <= d:
        return

    visited[x][y] = True

    for t in range(4):
        nx = x + dx[t]
        ny = y + dy[t]

        if nx >= N or ny >= N or nx < 0 or ny < 0:
            continue
        
        if graph[nx][ny] > d and visited[nx][ny] == 0:
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
                if graph[i][j] > d:
                    count += 1
                    dfs(i,j,d)

                else:
                    continue
    
    visited = [[False] * N for _ in range(N)]
    max_count.append(count)    
    count = 0
if max(max_count) > 1:
    print(max(max_count))
else:
    print(1)


## 코드 수정 + 중간에 멈출 방법 찾기
