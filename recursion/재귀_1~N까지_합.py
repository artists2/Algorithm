# 바킹독 1~N까지 합 재귀 연습


def ssum(N):
    if not N:
        return 0
    return N + ssum(N-1)

N = int(input())
print(ssum(N))