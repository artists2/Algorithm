n = int(input())

result = [0, 1]

for i in range(0, n-1):
    result.append(result[i] + result[i+1])
if n==0: print(0)
else: print(result[-1])
