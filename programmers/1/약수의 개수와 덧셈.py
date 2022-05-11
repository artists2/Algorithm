def calc(n):  # 짝수면 True, 홀수면 False
    r = False
    count = 1
    for i in range(1, n//2+1):
        if n % i == 0:
            count += 1
    if count % 2 == 0:
        r = True
    return r


def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if calc(i):
            answer += i
        else:
            answer -= i
    return answer

print(solution(13, 17))  # 43
print(solution(24, 27))  # 52

#  약수가 홀수개인 모든 수는 제곱수