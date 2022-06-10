from itertools import permutations

def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    result = set()

    for i in range(1, len(numbers)+1):
        for per in permutations(numbers, i):
            result.add(int(''.join(per)))

    for r in result:
        if isPrime(r):
            answer += 1

    return answer


print(solution("17"))  # 3
print(solution("011"))  # 2