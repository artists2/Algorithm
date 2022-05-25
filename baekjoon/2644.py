from collections import deque

n = int(input())
start, end = list(map(int, input().split()))
m = int(input())


family = [[] for _ in range(n+1)]

for i in range(1, m+1):
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)

visited = [False] * (n+1)
d = [0] * (n+1)


def bfs(start):
    visited[start] = True
    q = deque()
    q.append(start)

    while q:
        e = q.popleft()

        for i in family[e]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                d[i] = d[e]+1
                
bfs(start)
if d[end] < 1:
    print(-1)
else:
    print(d[end])