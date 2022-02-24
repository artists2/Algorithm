# 부분 합

N, S = map(int,input().split())
lst = list(map(int,input().split()))

start, end = 0, 0
r = lst[0]
answer = 100001
 
while 1:
    if r >= S:
        r -= lst[start]
        answer = min(answer, end - start + 1)
        start += 1
    else:
        end += 1
        if end == N:
            break
        r += lst[end]
 
if answer == 100001:
    print(0)
else:
    print(answer)
