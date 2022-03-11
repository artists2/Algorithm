def solution(heights):
    answer = [0]
    tmp = []
    for i in range(len(heights)-1, 0, -1): # 역순
        for j in range(i-1, -1, -1):
            if heights[i] < heights[j]:
                tmp.append(j+1)
                break
            elif j == 0:
                tmp.append(0)
    for i in reversed(tmp):
        answer.append(i)        
        
    return answer

