# 부등호

k = int(input())
iqs = list(input().split())

max_num, min_num = '', ''

visited = [False] * 10

def check(i, j, k: str):
    if k == '<':
        return i < j
    else:
        return i > j

def dfs(n, s):
    global max_num, min_num

    if n == k+1:
        if not len(min_num):
            min_num = s
        else:
            max_num = s
        return
    
    for i in range(10):
        if not visited[i]:
            if n == 0 or check(s[-1], str(i), iqs[n-1]):
                print(visited)
                visited[i] = True
                dfs(n+1, s+str(i))
                visited[i] = False


dfs(0, '')
print(max_num)
print(min_num)