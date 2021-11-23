n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
result = 0

for i in range(1, n+1):
    if k == 0:
        break
    result += (k // a[-i])
    k = (k % a[-i])

print(result)