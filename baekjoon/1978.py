N = int(input())

nums = list(map(int, input().split()))
count = 0
def eratosthenes(num: int) -> bool:  # 함수이름은 그냥 임시로 지은거임..
    for i in range(2, num-1):
        if num % i == 0:
            return False
    return True

for n in nums:
    if n == 1:
        continue
    if n == 2:
        count += 1
        continue

    if eratosthenes(n):
        count += 1
    else:
        continue


print(count)