import sys
sys.setrecursionlimit(10000)


T = int(input())

dx = [-1, 1, 0, 0]  # 좌 우
dy = [0, 0, -1, 1]  # 하 상

result = []

def dfs(x, y):
    if x < 0 or x >= N or y <0 or y >= M:
        return False
    if graph[x][y]:
        graph[x][y] = 0  # 방문체크
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            dfs(cx, cy)
        return True
    return False
        


count = 0

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]


    for i in range(K):
        b, a = map(int, input().split())
        graph[a][b] = 1

    for n in range(N):
        for m in range(M):
            if dfs(n, m):  # 덩어리 하나 발견 할 때 마다 
                count += 1
    result.append(count)
    count = 0

    # print(M, N, K)
    # for i in graph:
    #     print(i)

for r in result:
    print(r)

