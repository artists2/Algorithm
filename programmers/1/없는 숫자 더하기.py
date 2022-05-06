def solution(numbers):
    answer = 0
    check = [False for i in range(10)]
    for num in numbers:
        check[num] = True
    
    for i, c in enumerate(check):
        if not c:
            answer += i

    return answer


print(solution([1,2,3,4,6,7,8,0]))  # 14
print(solution([5,8,4,0,6,7,9]))  # 6