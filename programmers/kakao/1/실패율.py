def solution(N, stages):
    answer = []
    result = []
    for stage in range(1, N+1):
        challenge = 0
        not_clear = 0
        r = 0
        for user in stages:
            if user >= stage:
                challenge += 1
                if user == stage:
                    not_clear += 1
        if challenge:
            r = (not_clear / challenge)
        else: 
            r = 0
        result.append((stage, r))
    result.sort(key=lambda x: x[1], reverse=True)
    for r in result:
        answer.append(r[0]) 
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))  # [3, 4, 2, 1, 5]
print(solution(4, [4, 4, 4, 4, 4]))  # [4, 1, 2, 3]


# 실패율 = 스테이지에 도달 했으나, 아직 클리어 하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어의 수