# 치킨배달 
# 0 빈칸 1 집 2 치킨집
from sys import stdin
from itertools import combinations

N, M = map(int, input().split())

result = 9999999

maps = []
homes = []
chk = []


for _ in range(N):
    maps.append(list(map(int, stdin.readline().split())))

for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            homes.append((i, j))
        if maps[i][j] == 2:
            chk.append((i, j))


for ch in combinations(chk, M):
    temp = 0
    for h in homes:
        c = 100000
        for j in range(M):
            c = min(c, abs(h[0] - ch[j][0]) + abs(h[1] - ch[j][1]))
        temp += c
    result = min(result, temp)

for ch in combinations(chk, M):
    for h in homes:
        for j in range(M):
            print(h[0], ch[j][0], h[1], ch[j][1], "----", ch, h, j)

# print(result)
