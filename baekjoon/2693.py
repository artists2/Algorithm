import sys
N = int(input())

array = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in array:
    i.sort()
    print(i[-3])
    # print(sorted(i)[-2])
# print(array)