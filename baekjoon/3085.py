# 사탕게임
# check 함수 (오른쪽, 밑만 체크)

N = int(input())

board = []


for _ in range(N):
    board.append(list(input()))


def check(board, N, count):
    max_count = 0

    for i in range(N):
        count = 1
        for j in range(N-1):
            if board[i][j] == board[i][j+1]:
                count += 1
                max_count = max(count, max_count)
            else:
                count = 1

    for i in range(N):
        count = 1
        for j in range(N-1):
            if board[j][i] == board[j+1][i]:
                count += 1
                max_count = max(count, max_count)
            else:
                count = 1
        count = 1
    if max_count == 1:
        return 0
    return max_count
    
answer = (check(board, N, 1))

for i in range(N):
    for j in range(N-1):
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        answer = max(answer, check(board, N, 1))
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

for i in range(N):
    for j in range(N-1):
        board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
        answer = max(answer, check(board, N, 1))
        board[j][i], board[j+1][i] = board[j+1][i], board[j][i]

print(answer)
