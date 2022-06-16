def solution(n):
    answer = 0
    check = [False] * (n+1)
    
    for i in range(2, n+1):
        if not check[i]:
            answer += 1
            for j in range(i, n+1, i):
                check[j] = True

    return answer