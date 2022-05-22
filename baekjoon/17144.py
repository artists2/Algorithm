import sys
from collections import deque

input = sys.stdin.readline

R, C, T = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(R)]
check = [[0 for _ in range(C)] for _ in range(R)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
answer = 2
up = -1
down = -1

for i in range(R):
    if board[i][0] == -1:
        up = i
        down = i+1
        break

def diffusion(r, c, check):
    e = board[r][c] // 5
    targets = []

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nc < 0 or nr >= R or nc >= C or (board[nr][nc] == -1):
            continue
        targets.append((nr, nc))
    
    for target_r, target_c in targets:
        check[target_r][target_c] += e
    board[r][c] = board[r][c] - (e * len(targets))
    
    return check


def circulation_up():  # 반시계
    dr = [0, -1, 0, 1]  # *순서 중요
    dc = [1, 0, -1, 0]
    d = 0
    backup = 0
    r, c = up, 1
    while True:
        nr = r + dr[d]
        nc = c + dc[d]
        if r == up and c == 0:
            break
        if nr < 0 or nc < 0 or nr >= R or nc >= C:
            d += 1
            continue
        board[r][c], backup = backup, board[r][c]
        r = nr
        c = nc
    return


def circulation_down():  # 시계
    dr = [0, 1, 0, -1]  # 순서 중요
    dc = [1, 0, -1, 0]
    d = 0
    backup = 0
    r, c = down, 1  # start 지점
    while True:
        nr = r + dr[d]
        nc = c + dc[d]
        if r == down and c == 0:
            break
        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            d += 1
            continue
        board[r][c], backup = backup, board[r][c]
        r = nr
        c = nc
    return


def spread():
    check = [[0 for _ in range(C)] for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if board[r][c] and board[r][c] != -1:
                check = diffusion(r, c, check)

    for r in range(R):
        for c in range(C):
            board[r][c] += check[r][c]
    return


for time in range(T):
    spread()
    circulation_up()
    circulation_down()


for r in range(R):
    for c in range(C):
        answer += board[r][c]

print(answer)
