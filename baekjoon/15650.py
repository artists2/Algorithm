# N과 M (2)

N, M = map(int, input().split())

s =[]


def dfs(n, m, s, start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(start, n+1):
        if i in s:
            continue
        s.append(i)
        dfs(n, m, s, i)
        s.pop()


dfs(N, M, s, 1)
