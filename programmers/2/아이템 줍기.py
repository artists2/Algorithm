from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    DOUBLE_FUNC = lambda x : x*2
    SIZE = DOUBLE_FUNC(51)
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    board = [[0 for _ in range(SIZE)] for _ in range(SIZE)]


    for r in rectangle:
        r = map(DOUBLE_FUNC, r)
        x1, y1, x2, y2 = r
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                board[i][j] = 1
    
    for r in rectangle:
        r = map(DOUBLE_FUNC, r)
        x1, y1, x2, y2 = r
        for i in range(x1+1, x2):
            for j in range(y1+1, y2):
                board[i][j] = 0


    characterX = DOUBLE_FUNC(characterX)
    characterY = DOUBLE_FUNC(characterY)
    itemX = DOUBLE_FUNC(itemX)
    itemY = DOUBLE_FUNC(itemY)
    
    q = deque()
    q.append((characterX, characterY))

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nc < 0 or nr >= SIZE or nc >= SIZE:
                continue
            if board[nr][nc] == 1:
                board[nr][nc] += board[r][c]
                q.append((nr,nc))

    answer = (board[itemX][itemY]) // 2
        

    return answer


print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))  # 17
print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1))  # 11
print(solution([[1,1,5,7]], 1, 1, 4, 7))  # 9
print(solution([[2,1,7,5],[6,4,10,10]], 3, 1, 7, 10))  # 15
print(solution([[2,2,5,5],[1,3,6,4],[3,1,4,6]], 1, 4, 6, 3))  # 10