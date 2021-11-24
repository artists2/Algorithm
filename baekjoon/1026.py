N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

result = 0

for i in range(0, N):
    result += A[i] * B[i]

print(result)

