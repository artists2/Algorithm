# 인구 이동
from collections import deque

n, l, r = map(int, input().split(' '))
graph = [list(map(int, input().split(' '))) for _ in range(n)]

d_x = [-1, 0, 1, 0]
d_y = [0, 1, 0, -1]

is_move = False


def bfs(c_x, c_y, visited, grpah):
    global is_move
    people = graph[c_x][c_y]
    count = 1
    queue = deque()
    queue.append((c_x, c_y))
    visited[c_x][c_y] = True
    temp = list()
    temp.append((c_x, c_y))

    while queue:
        pop_x, pop_y = queue.popleft()

        for i in range(4):
            n_x = pop_x + d_x[i]
            n_y = pop_y + d_y[i]

            if n_x < 0 or n_x >= n or n_y < 0 or n_y >= n:
                continue

            if visited[n_x][n_y]:
                continue

            if l <= abs(grpah[pop_x][pop_y] - grpah[n_x][n_y]) <= r:
                visited[n_x][n_y] = True
                queue.append((n_x, n_y))
                people += graph[n_x][n_y]
                count += 1
                temp.append((n_x, n_y))

    move_people = people // count

    if count > 1:
        is_move = True
        for x, y in temp:
            graph[x][y] = move_people

answer = 0

while True:
    is_move = False
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j, visited, graph)

    if is_move:
        answer += 1
    else:
        break

print(answer)


# from collections import deque
# import copy


# N, L, R = map(int, input().split())

# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]
# count = 0
# land = []
# visited = [[[False, False] for _ in range(N)] for _ in range(N)]  # [visited, line]

# for _ in range(N):
#     land.append(list(map(int, input().split())))

# # 1. land를 돌면서 오른쪽, 밑을 체크 하고 뚫리는지 체크 (check)
# # 2. 합쳐서 출력

# # print(visited)

# def bfs(r, c):
#     visit = copy.deepcopy(visited)
#     stack = []
#     union = 0


#     q = deque()
#     q.append((r, c))
#     stack.append((r, c))

#     while q:
#         r, c = q.popleft()
#         visit[r][c][0] = True
#         visit[r][c][1] = True

#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]

#             if nr < 0 or nc < 0 or nr >= N or nc >= N:
#                 continue
#             if visit[nr][nc][0]:
#                 continue

#             if abs(land[r][c] - land[nr][nc]) >= L and abs(land[r][c] - land[nr][nc]) <= R:
#                 # print(abs(land[r][c] - land[nr][nc]), L, abs(land[r][c] - land[nr][nc]), R)
#                 q.append((nr, nc))
#                 stack.append((nr, nc))
#                 # print(nr, nc)
#     if len(stack) == 1:
#         return False
    
#     for i, j in stack:
#         union += land[i][j]
    
#     union = union // len(stack)
#     # print(union)
#     for i, j in stack:
#         land[i][j] = union
#     return True


# # for l in land:
# #     print(l)

# # print()
# print(count)