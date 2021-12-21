# 팩토리얼

def factorial(N: int) -> int:
    result = 1
    if N < 2:
        return result
    else:
        return N * factorial(N-1)

# N = int(input())
# print(factorial(N))
print(factorial(int(input())))