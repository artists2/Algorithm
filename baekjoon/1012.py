T = int(input())

def dfs(x, y):
    if x < 0 or x >=M or y <0 or y >= N:
        False
    if graph[x][y]:
        pass





for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]


    for i in range(K):
        b, a = map(int, input().split())
        graph[a][b] = 1

    print(M, N, K)
    for i in graph:
        print(i)


