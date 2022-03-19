# N과 M (1)

N, M = map(int, input().split())

s = []

def dfs(n, m, s):

    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, n + 1):
        if i in s:
            continue
        # print(i)
        s.append(i)
        dfs(n, m, s)
        s.pop()

dfs(N, M, s)

