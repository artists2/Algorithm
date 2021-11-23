import itertools

n = int(input())
p = (list(map(int, input().split())))
p.sort()

p = list(itertools.accumulate(p))

result = sum(p)

print(result)