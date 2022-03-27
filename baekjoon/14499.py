# 주사위 굴리기
import sys

n, m, x, y, k = map(int, input().split())

maps = []

for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))

order = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0]  # 위, 뒤, 오른쪽, 왼쪽, 앞, 밑

def tumble(order: int) -> None:
    if order == 1:  # 동
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    if order == 2:  # 서
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    if order == 3:  # 북
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    if order == 4:  # 남
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]

for od in order:
    if od == 1:  # 오
        if y + 1 > (m - 1):
            continue
        else:
            y += 1
            tumble(od)
    if od == 2:  # 왼
        if y - 1 < 0:
            continue
        else:
            y -= 1
            tumble(od)
    if od == 3:  # 위
        if x - 1 < 0:
            continue
        else:
            x -= 1
            tumble(od)
    if od == 4:  # 아래
        if x + 1 > (n - 1):
            continue
        else:
            x += 1
            tumble(od)
    print(dice[0])
    if maps[x][y] == 0:
        maps[x][y] = dice[5]
    else:
        dice[5] = maps[x][y]
        maps[x][y] = 0
