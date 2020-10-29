def solution(n): #n의 제곱근 이하의 소수만 판별 해 내면 됨.
    a = [False, False] + [True] * (n-1)
    for i in range(2, int(n ** 0.5)+1):
        if a[i]:
            for j in range(i*2, n+1, i):
                a[j] = False
                
    return a.count(True)


출처: https://ggn0.tistory.com/99?category=695152 [Not null] #풀이 과정