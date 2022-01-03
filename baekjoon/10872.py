# 팩토리얼

def factorial(N: int) -> int:
    result = 1
    if N < 2:
        return result
    else:
        return N * factorial(N-1)

print(factorial(int(input())))
