def solution(n, times):
    times.sort()
    answer = 0
    start = 1 # 1초 걸리는 심사관에게 모두 검사를 받을 때
    end = times[-1] * n  # 제일 느린 심사관에게 모두 검사를 받을때

    while start <= end:
        mid = (start + end) // 2
        p = 0
        for t in times:  # p는 모든 심사관들이 mid분 동안 심사한 사람의 수
            p += mid // t
            print(start, end, mid, t, p)

            if p >= n:  # 모든 심사관을 거치지 않아도 n명이상 검사를 수행 한 경우엔 break
                break

        # 심사한 사람의 수가 심사 받아야 할 사람의 수(n)보다 많거나 같은 경우 end = mid -1 로 조정
        if p >= n:
            answer = mid
            end = mid - 1
        elif p < n:  # 심사한 사람의 수가 심사 받아야 할 사람의 수(n)보다 작은 경우 start = mid + 1
            start = mid + 1

    return answer


print(solution(6, [7, 10]))  # 28
print(solution(6, [1, 10]))  # 6
print(solution(2, [4, 10]))  # 8
print(solution(4, [1, 2]))  # 3
# start, end, mid를 시간으로 표현하여 적절한 시간에 모든 사람을 검사할 수 있는지 -> 
# 
