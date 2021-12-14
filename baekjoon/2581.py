M = int(input())
N = int(input())

result = []
def eratosthenes(num: int) -> bool:  # 함수이름은 그냥 임시로 지은거임..
    if num == 1:
        return False
    for i in range(2, num-1):
        if num % i == 0:
            return False
    return True

for i in range(M, N+1):
    if eratosthenes(i):
        result.append(i)
    else:
        continue
# print(result)

if result:
    print(sum(result))
    print(min(result))
else:
    print(-1)