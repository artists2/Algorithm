def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    answer = []

    number_of_case = 0
    count = 0
    
    for lotto_num in lottos:
        if lotto_num == 0:
            number_of_case += 1
            continue

        if lotto_num in win_nums:
            count += 1
    
    answer.append(rank[count+number_of_case])
    answer.append(rank[count])

    return answer