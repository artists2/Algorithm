
f = True
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(place, r, c, X, Y, cnt):
    global f
    if cnt == 2:
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nc < 0 or nr >= 5 or nc >= 5 or place[nr][nc] == "X":
            continue
        if nr == X and nc == Y:  # 처음 dfs문을 들어온 좌표를 제외해줘야함.....(주석)
            continue
        if place[nr][nc] == "P":
            f = False
            return
        dfs(place, nr, nc, X, Y, cnt+1)
    return
def solution(places):
    global f
    answer = []

    for wait in range(5):
        flag = True
        for r in range(5):
            for c in range(5):
                if places[wait][r][c] == "P":
                    f = True
                    dfs(places[wait], r, c, r, c, 0)
                    if not f: 
                        flag = False

        if flag:
            answer.append(1)
        else:
            answer.append(0)

    return answer



print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))

# [1, 0, 1, 1, 1]
# 두 테이블 T1, T2가 행렬 (r1, c1), (r2, c2)에 각각 위치하고 있다면, T1, T2 사이의 맨해튼 거리는 |r1 - r2| + |c1 - c2| 입니다. ↩

"""
P0000 -> 이경우 S에서 탐색을 좌우지간 1칸씩 움직이게 되는데 이때, 처음 들어온 dfs 부분인 P를 count 하여 False가 됨.
S0000 -> 그래서 처음 들어온 좌표를 X, Y 로 저장해두고 다음 챕터때 들어온 좌표를 스캔하려고 하면 continue
00000 -> count 는 깊이.. 

"""