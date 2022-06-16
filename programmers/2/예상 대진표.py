def solution(n,a,b):
    answer = 0
    while a!=b:
        answer += 1

        a, b = (a+1)//2, (b+1)//2
        print(a, b)
    return answer


print(solution(1000000, 2323, 231))