from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    q = deque()
    q.append([0, 0])
    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            else:
                if maps[nr][nc] == 1:
                    maps[nr][nc] += maps[r][c]
                    q.append([nr, nc])
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))  
# 11
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))  
# -1