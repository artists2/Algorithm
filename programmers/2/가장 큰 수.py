def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    answer = str(int(''.join(numbers)))
    return answer


print(solution([6, 10, 2]))  # "6210"
print(solution([3, 30, 34, 5, 9]))  # "9534330"
print(solution([9, 98, 999, 1000, 8]))  # "99999981000"



# 시간초과

# from itertools import permutations

# def solution(numbers):
#     answer = []
#     numbers = list(map(str, numbers))

#     for per in permutations(numbers, len(numbers)):
#         answer.append(int(''.join(per)))

#     return str(max(answer))

