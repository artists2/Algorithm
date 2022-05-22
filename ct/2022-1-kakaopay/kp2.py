def solution(n, m, rectangle):
    answer = []
    board = [[0 for _ in range(n)] for _ in range(m)]
    rectangle.sort(key=lambda x: x[0])

    for r in range(m):
        for c in range(n):
            for square in rectangle:
                for loop in range(square[1]):
                    flag = 0
                    # 검사
                    if (r-1 + square[0]) >= m or (c-1 + square[0]) >= n:  # 범위가 벗어나는지
                        flag = 1
                        
                    if not flag:
                        for i in range(square[0]):  # 사각형 방향 다른사각형 있는지
                            for j in range(square[0]):
                                if board[r+i][c+j]:
                                    flag = 1
                                    break
                                if flag:
                                    break
                            if flag:
                                break

                    
                    if not flag:
                        for i in range(square[0]):
                            for j in range(square[0]):
                                board[r+i][c+j] = 1
                        answer.append([c, r, square[0]])
                        square[1] -= 1
    for b in board:
        print(b)

    return answer

print(solution(7, 8, [[2,2],[1,4],[3,2]]))
# # [[0,0,1],[1,0,1],[2,0,1],[3,0,1],[4,0,2],[0,1,2],[2,2,3],[0,5,3]]
# print(solution(3, 3, [[1,1]]))
# # [[0,0,1]]