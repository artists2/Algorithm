def solution(N, number):
    answer = -1
    dp = []

    for i in range(1, 9):
        tmp = [int(str(N) * i)]
        for j in range(0, i-1):
            for a in dp[j]:
                for b in dp[-j-1]:
                    tmp.append(a + b)
                    tmp.append(a - b)
                    tmp.append(a * b)
                    if b:
                        tmp.append(a // b)
        tmp = set(tmp)
        
        if number in tmp:
            answer = i
            break

        dp.append(tmp)
    
    return answer


print(solution(5, 12))
print(solution(2, 11))
# Back-Tracking + Memoization