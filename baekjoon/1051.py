# 숫자 정사각형

N, M = map(int, input().split())

square = []
answer = 0

for _ in range(N):
    square.append(list(map(int, list(input()))))

x = min(N, M)

for r in range(N):
    for c in range(M):
        for p in range(x):
            if r+p < N and c+p < M:
                if square[r][c] == square[r+p][c] == square[r][c+p] == square[r+p][c+p]:
                    answer = max(p, answer)

print((answer+1) ** 2)