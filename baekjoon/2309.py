from itertools import combinations

dwarfs = [int(input()) for _ in range(9)]
result = []
for i in combinations(dwarfs, 7):
    if sum(i) == 100:
        for j in i:
            result.append(j)
        break

for _ in sorted(result):
    print(_)