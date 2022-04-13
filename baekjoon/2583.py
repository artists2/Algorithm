# 영역 구하기
import sys
sys.setrecursionlimit(10000)

M, N, K = map(int, input().split())

graph = [[0] * M for _ in range(N)]
count = 0
result = []

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for r in range(x1, x2):
        for c in range(y1, y2):
            graph[r][c] = 1

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def dfs(r, c):
    global _count
    
    graph[r][c] = 1
    _count += 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nc < 0 or nr >= N or nc >= M:
            continue
        if not graph[nr][nc]:
            dfs(nr, nc)
    return


for n in range(N):
    for m in range(M):
        if not graph[n][m]:
            _count = 0
            count += 1
            dfs(n, m)
            result.append(_count)

answer = ''
for r in sorted(result):
    answer += str(r)
    answer += ' '

print(count)
print(answer)


# 좌표 다듬기
# 직사각형 색칠하기
# 색칠 안되어 있는 곳 탐색하고 탐색 횟수 카운팅
# 탐색 할때 안에 색칠 안되어있는 곳 카운팅