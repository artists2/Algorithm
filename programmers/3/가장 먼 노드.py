from collections import deque


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [[False, 0] for _ in range(n+1)]

    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)

    def bfs(start):
        q = deque([[start, 0]])
        
        visited[start] = [True, 0]  # 

        cnt = 0
        while q:
            v, cnt = q.popleft()
            cnt += 1
            for i in graph[v]:
                if not visited[i][0]:
                    q.append([i, cnt])
                    visited[i][0] = True
                    visited[i][1] = cnt

    bfs(1)

    tmp = visited[:]
    tmp.sort(key= lambda x : x[1])

    max_cnt = tmp[-1][1]
    for v1, v2 in visited:
        if v2 == max_cnt:
            answer += 1
        
    return answer




print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))  # 3