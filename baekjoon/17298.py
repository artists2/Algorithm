import sys
input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))
answer = [-1] * N
stck = []

for i in range(N):
    while stck and (stck[-1][1] < numbers[i]):
        idx, number = stck.pop()
        answer[idx] = numbers[i]
    stck.append((i, numbers[i]))

print(*answer)