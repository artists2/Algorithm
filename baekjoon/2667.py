# 단지번호붙이기

from itertools import count
import sys

N = int(input())  # 라인 수

maps = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

dx = [-1, 1, 0, 0]  # 좌 우
dy = [0, 0, -1, 1]  # 하 상

def dfs(x, y):
    if x<0 or x>=N or y<0 or y>= N:  # x좌표 -이탈 or x좌표 N이상 이탈 or y좌표 -이탈 or y좌표 N이상 이탈 시
        return False

    if maps[x][y]:  # 단지를 발견하면 탐색시작
        global count
        count += 1
        maps[x][y] = 0  # 방문 표시

        for i in range(4):  # 상하 좌우에 대한 좌표 써치
            cx = x + dx[i]
            cy = y + dy[i]
            dfs(cx, cy)
        return True
    return False

count = 0
result = []

for i in range(N):
    for j in range(N):
        if dfs(i, j):
            result.append(count)
            count = 0

print(len(result))

for r in sorted(result):
   print(r)
