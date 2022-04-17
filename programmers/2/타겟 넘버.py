answer = 0

def dfs(i, v, numbers, target):
    global answer
    if i == len(numbers):
        if v == target:
            answer += 1
            return        
        return 

    dfs(i+1, v+numbers[i], numbers, target)
    dfs(i+1, v-numbers[i], numbers, target)
    return


def solution(numbers, target):
    global answer

    dfs(0, 0, numbers, target)

    return answer


print(solution([1, 1, 1, 1, 1], 3))  # 5

print(solution([4, 1, 2, 1], 4))  # 2