def solution(arrangement):
    answer = 0
    lst = []
    arrangement = arrangement.replace("()", "x")
    print(arrangement)
    for i in range(0, len(arrangement)):
        if arrangement[i] == '(':
            lst.append(1)
        elif arrangement[i] == ')':
            answer += lst.pop()
        elif arrangement[i] == 'x':
            answer += lst.count(1)
    return answer


# 포인트 : append, pop 즉 스택을 이용한 쇠막대기의 구현
