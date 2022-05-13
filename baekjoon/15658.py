N = int(input())

numbers = list(map(int, input().split()))

add, sub, mul, div = (map(int, input().split()))  # [+, -, *, //]

max_num, min_num = -1000000000, 1000000000

def dfs(depth, res, add, sub, mul, div):
    global max_num, min_num

    if depth == N:
        if max_num < res:
            max_num = res
        if min_num > res:
            min_num = res
        return

    if add:
        dfs(depth+1, res + numbers[depth], add-1, sub, mul, div)
    if sub:
        dfs(depth+1, res - numbers[depth], add, sub-1, mul, div)
    if mul:
        dfs(depth+1, res * numbers[depth], add, sub, mul-1, div)
    if div:
        dfs(depth+1, int(res / numbers[depth]), add, sub, mul, div-1)

dfs(1, numbers[0], add, sub, mul, div)

print(max_num)
print(min_num)