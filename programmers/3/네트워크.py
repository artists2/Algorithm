def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j]:
                graph[i].append(j)

    def dfs(n):
        visited[n] = True
        
        for g in graph[n]:
            if not visited[g]:
                dfs(g)
        return


    for i in range(0, n):
        if not visited[i]:
            answer += 1
            dfs(i)

    return answer

print(solution(3, [[1,1,0], [1,1,0], [0,0,1]])) # 2
print(solution(3, [[1,1,0], [1,1,1], [0,1,1]])) # 1