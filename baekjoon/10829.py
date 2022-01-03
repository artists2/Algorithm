# 이진수 변환 재귀

def binary(N: int):
    bin_string: str = ''
    if N == 1:
        return "1" + bin_string
    if N == 0:
        return "0" + bin_string
    else:
        return binary(N//2) + str(N % 2)

print(binary(int(input())))