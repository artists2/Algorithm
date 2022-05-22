def solution(region, num, info):
    answer = [-1 for _ in range(len(info))]
    winner = []
    user_info = [[] for _ in range(4)]
    for n, infos in enumerate(info, start=1):
        home, homeless, join, family = infos[0], infos[1], infos[2], infos[3]
        user_info[home].append((n, (homeless + 1) * 2 + (join + 2) + (family * 5)))
        user_info[home].sort(key=lambda x : x[1], reverse=True)

    if len(user_info[region]) >= num:
        for add in user_info[region][:num]:
            winner.append(add)
    else:
        for add in user_info[region][:num]:
            winner.append(add)
        temp = []
        for i, user in enumerate(user_info):
            if i == region:
                continue
            for u in user:
                temp.append(u)
        temp.sort(key=lambda x : x[1], reverse=True)
        for add in temp[:(num-len(winner))]:
            winner.append(add)
    for i, win in enumerate(winner, start=1):
        answer[win[0]-1] = i
    print(answer)

    return answer


print(solution(2, 4, [[1, 0, 2, 1], [2, 6, 5, 2], [3, 10, 2, 4], [1, 1, 5, 6], [2, 7, 10, 2], [3, 8, 6, 3]]))
print(solution(3, 2, [[3, 8, 6, 2], [1, 12, 5, 2], [3, 2, 9, 5], [3, 6, 10, 1], [1, 10, 5, 3]]))
print(solution(1, 7, [[1, 0, 2, 1], [2, 6, 5, 2], [3, 10, 2, 4], [1, 1, 5, 6], [2, 7, 10, 2], [3, 8, 6, 3]]))


