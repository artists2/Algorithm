import sys

stations = [tuple(map(int,sys.stdin.readline().split())) for _ in range(10)]
result = []
people = 0
for station in stations:
    people -= station[0]
    people += station[1]
    result.append(people)

print(max(result))
    