# N 과 M (4)

N, M = map(int, input().split())

s = []

def dfs(N, M):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, N+1):
        if s and s[-1] > i:
            continue
        s.append(i)
        dfs(N, M)
        s.pop() 

dfs(N, M)



##### 다른 풀이2

n,m = map(int, input().split())
 
s = []
 
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start, n+1):
        s.append(i)
        dfs(i)
        s.pop()
    
dfs(1)