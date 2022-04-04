def solution(rows, columns, queries):
    maps = []
    answer = []
    for r in range(rows):
        maps.append([i for i in range(r*columns+1, (r + 1) * columns + 1)])

    for q in queries:
        q = list(map(lambda x: x-1, q))
        x1, y1, x2, y2 = q[0], q[1], q[2], q[3]
        tmp = maps[x1][y1]
        mini = []
        
        for r in range(x1 + 1, x2 + 1):
            maps[r-1][y1] = maps[r][y1]
            mini.append(maps[r][y1])
        
        for c in range(y1 + 1, y2 + 1):
            maps[x2][c-1] = maps[x2][c]
            mini.append(maps[x2][c])

        for r in range(x2 - 1, x1 - 1, -1):
            maps[r+1][y2] = maps[r][y2]
            mini.append(maps[r][y2])
        
        for c in range(y2 - 1, y1 - 1, -1):
            maps[x1][c+1] = maps[x1][c]
            mini.append(maps[x1][c])
        
        maps[x1][y1+1] = tmp
        mini.append(maps[x1][y1+1])
        
        answer.append(min(mini))
    return answer

    


    

    



print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
print(solution(100, 97, [[1,1,100,97]]))