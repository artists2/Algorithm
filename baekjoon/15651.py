# N과 M (3)

N, M = map(int, input().split())

s = []

def dfs(N, M):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in range(1, N + 1):
        s.append(i)
        dfs(N, M)
        s.pop()

dfs(N, M)