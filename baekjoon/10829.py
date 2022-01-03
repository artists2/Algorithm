# 이진수 변환 재귀

def binary(N: int):
    if N == 1:
        return "1" 
    if N == 0:
        return "0" 
    else:
        return binary(N//2) + str(N % 2)

print(binary(int(input())))