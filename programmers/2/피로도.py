from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for i in reversed(range(1, len(dungeons)+1)):
        for per in permutations(dungeons, i):
            tmp = 0
            tmp_k = k
            for d in per:
                m_p, e_p = d[0], d[1]
                if tmp_k >= m_p:
                    tmp_k -= e_p
                    tmp += 1
                else:
                    continue
            answer = max(tmp, answer)
            
            if answer == i:
                return answer

    return answer

#print(solution(80, [[80,20],[50,40],[30,10]]))  # 3
print(solution(40, [[40, 20], [10, 10], [10, 10], [10, 10], [10, 10]]))  # 4





# 그리디 문제인줄

# def solution(k, dungeons):
#     answer = 0
#     dungeons.sort(key=lambda x : x[0])
#     dungeons.sort(key=lambda x : x[1])
#     dungeons.sort(key= lambda x :x[0]-x[1], reverse=True)
#     print(dungeons)
#     for d in dungeons:
#         m_p, e_p = d[0], d[1]
#         if k >= m_p:
#             k -= e_p
#             answer += 1
#         else:
#             continue
#     return answer
