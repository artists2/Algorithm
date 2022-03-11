def solution(prices):
    answer = []
    
    for i in range(0, len(prices)-1): # (0,3) 0,1,2
        for j in range(i+1, len(prices)): # 1,4 1,2,3
            if prices[i] > prices[j]:
                answer.append(j-i)
                break
            if j == len(prices)-1:
                answer.append(j-i)
    
    answer.append(0)
    return answer


