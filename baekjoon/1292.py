A, B = map(int, input().split())
result = 0
seq = []

for i in range(1, B+1):
    for j in range(i):
        seq.append(i)
print(sum(seq[A-1:B]))
