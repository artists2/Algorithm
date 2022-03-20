#공주님의 정원
import sys

N = int(input())

flowers = []

end = 0
target = 301
count = 0
for _ in range(N):
    (sm, sd, em, ed) = map(int, sys.stdin.readline().split())
    flowers.append((sm * 100 + sd, em * 100 + ed))

flowers.sort(key=lambda date: (date[0], date[1]))

while flowers:
    if target >= 1201 or target < flowers[0][0]:
        break
    for _ in range(len(flowers)):
        if target >= flowers[0][0]:
            if end <= flowers[0][1]:
                end = flowers[0][1]
            flowers.remove(flowers[0])
        else:
            break
    target = end
    count += 1

if target < 1201:
    print(0)
else:
    print(count)
