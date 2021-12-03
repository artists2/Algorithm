N, K = map(int, input().split())

divisor = []

for i in range(1, N+1):
    if N % i == 0:
        divisor.append(i)
    else:
        continue

try: print(divisor[K-1])
except: print(0)

