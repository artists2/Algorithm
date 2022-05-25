import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))
counter_number = Counter(numbers)

answer = [-1] * N
stack = []

for i in range(N):
    while stack and counter_number[stack[-1][1]] < counter_number[numbers[i]]:
        idx, number = stack.pop()
        answer[idx] = numbers[i]
    stack.append((i, numbers[i]))

print(*answer)