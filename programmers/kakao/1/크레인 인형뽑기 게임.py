def pick(board, size, n):  # size = N
    picked = 0
    for i in range(size):
        if board[i][n-1]:
            picked = board[i][n-1]
            board[i][n-1] = 0
            return (board, picked)
    return (board, picked)


def solution(board, moves):
    answer = 0
    N = len(board)
    stack = []
    
    for move in moves:
        board, p = pick(board, N, move)
        if stack:
            if stack[-1] == p:
                answer += 2
                stack.pop()
                continue
        if p:
            stack.append(p)
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))  # 4