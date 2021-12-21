# 바킹독 N~1까지 출력 재귀 연습

def pprint(N):
    if N == 0:
        return
    print(N)
    pprint(N-1)


N = int(input()) 
pprint(N)