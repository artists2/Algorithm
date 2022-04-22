n = int(input())

ans = 0
r = [0] * n

def check(x):
    for c in range(x):
        if r[x] == r[c] or abs(r[x] - r[c]) == abs(x - c):
            return False
    
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n): # [x, i]에 퀸을 놓겠다.
            r[x] = i
            if check(x):
                n_queens(x+1)

n_queens(0)
print(ans)
