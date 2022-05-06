from itertools import combinations

def check(lst):
    e = sum(lst)

    if e < 2:
        return False
    for i in range(2, e):
        if not (e % i):
            return False
    return True


def solution(nums):
    answer = 0
    for combi in combinations(nums, 3):
        if check(combi):
            answer += 1

    return answer


print(solution([1, 2, 3, 4]))  # 1
print(solution([1, 2, 7, 6, 4]))  # 4