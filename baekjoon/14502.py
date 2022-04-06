# 연구소

import copy
from itertools import combinations

N, M = map(int, input().split())

maps = []
result = []

for _ in range(N):
    maps.append(list(map(int, input().split())))

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
blank = []
virus = []

for r in range(N):
    for c in range(M):
        if maps[r][c] == 0:
            blank.append((r, c))
        if maps[r][c] == 2:
            virus.append((r, c))


def dfs(r, c):
    visited[r][c] = 2

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nc < 0 or nr >= N or nc >= M:
            continue
        if not visited[nr][nc]:
            dfs(nr, nc)


for a, b, c in combinations(blank, 3):
    visited = copy.deepcopy(maps)
    count = 0
    visited[a[0]][a[1]], visited[b[0]][b[1]], visited[c[0]][c[1]] = 1, 1, 1
    
    for r, c in virus:
        dfs(r, c)
    
    for v in visited:
        count += v.count(0)
    result.append(count)


print(max(result))


# 빈칸 (0)에 벽을 세울 수 있는 경우의 수를 구해서
# 벽 세우고
# dfs, bfs 탐색하면댐


# combinations 같은거로 0인좌표 저장한곳에 combinations(0좌표, 3) 이런식으로