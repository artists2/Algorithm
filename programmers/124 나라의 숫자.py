def solution(n):
    answer = ''
    lst = ['4', '1', '2']
    while (n > 0):
        s = n % 3
        n = n // 3
        if (s == 0):
            n -= 1;
        answer = lst[s] + answer
    return answer


