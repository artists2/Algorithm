# from collections import defaultdict

# def solution(n, results):
#     answer = 0
#     win, lose = defaultdict(set), defaultdict(set)
#     for w, l in results:
#         win[l].add(w)  
#         lose[w].add(l)  

#     for i in range(1, n + 1):
#         for w in win[i]:
#             lose[w].update(lose[i])
#         for l in lose[i]:
#             win[l].update(win[i])

#     for i in range(1, n + 1):
#         if len(win[i]) + len(lose[i]) == n - 1:
#             answer += 1
#     return answer


# 플로이드 워셜 
def solution(n, results):
    total = [['?' for i in range(n)] for j in range(n)]

    for i in range(n):
        total[i][i] = 'SELF'

    for result in results:
        total[result[0]-1][result[1]-1] = 'WIN'
        total[result[1]-1][result[0]-1] = 'LOSE'
    print(total)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if total[i][k] == 'WIN' and total[k][j] == 'WIN':
                    total[i][j] = 'WIN'
                elif total[i][k] == 'LOSE' and total[k][j] == 'LOSE':
                    total[i][j] = 'LOSE'

    answer = 0
    print(total)
    for i in total:
        if '?' not in i:
            answer += 1

    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))  # 2