def dfs(r ,c ,d, row, col, visited, grid):
    dr = [1, 0, -1, 0]
    dc = [0, -1, 0, 1]
    count = 0

    while True:
        if visited[r][c][d]:
            return count
        
        visited[r][c][d] = True

        r = (r + dr[d])  % row
        c = (c + dc[d])  % col

        if grid[r][c] == 'R':
            d = (d + 1) % 4
        elif grid[r][c] == 'L':
            d = (d + 3) % 4
        
        count += 1


def solution(grid):
    answer = []
    row, col = len(grid), len(grid[0])
    visited = [[[False] * 4 for _ in range(col)] for _ in range(row)]

    for r in range(row):
        for c in range(col):
            for d in range(4):
                if not visited[r][c][d]:
                    answer.append(dfs(r, c, d, row, col, visited, grid))
    
    answer.sort()

    return answer


print(solution(["SL","LR"]))  # [16]
print(solution(["S"]))  # [1, 1, 1, 1]
print(solution(["R","R"]))  # [4, 4]