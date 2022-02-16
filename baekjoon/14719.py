# 빗물

H, W = map(int, input().split())

block = list(map(int, input().split()))

result = 0


for i in range(1, W-1):
    left_max_block = max(block[:i])
    right_max_block = max(block[i+1:])
    smaller_block = min(left_max_block, right_max_block)

    if smaller_block > block[i]: # 더 작은 블록이 현재 블록보다는 크면 더해야함
        result += smaller_block - block[i]

print(result)
