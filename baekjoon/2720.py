# 세탁소 사장 동혁

T = int(input())
C = [int(input()) for _ in range(T)]

Q, D, N, P = 25, 10, 5, 1 
# Quarter -> cent
# Dime -> cent
# Nickel -> cent
# Penny -> cent

result = []
temp = 0

for i in C:
    result.append(i // Q)
    temp = i % Q
    result.append(temp // D)
    temp = temp % D
    result.append(temp // N)
    temp = temp % N
    result.append(temp // P)

for i in range(0, len(result), 4):
    print(result[i],result[i+1], result[i+2], result[i+3])    
    