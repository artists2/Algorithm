# 회의실 배정
N = int(input())
meeting = []
for _ in range(0, N):
    (start, end) = map(int, input().split())
    meeting.append((start, end))

meeting.sort(key = lambda x: (x[1], x[0]))
last_time = 0
result = 0

for i, j in meeting:
    if i >= last_time:
        result += 1
        last_time = j
print(result)

