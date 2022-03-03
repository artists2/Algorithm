# 수들의 합

S = int(input())

cnt = 0
result = 0

for i in range(1, 4294967295):
    if result > S:
        cnt -= 1
        break
    elif result == S:
        break
    else:
        result += i
        cnt += 1

print(cnt)