from collections import deque

def solution(priorities, location):
    answer = 0
    priorities[location] = str(priorities[location])
    catch = priorities[location]
    
    priorities = deque(priorities)
    print(priorities)
    while catch in priorities:
        flag = False
        e = priorities.popleft()

        for prior in priorities:
            if int(e) < int(prior):
                flag = True
                break
        
        if flag:
            priorities.append(e)
        else:
            answer += 1
            continue
        
    return answer

print(solution([2, 1, 3, 2], 2))  # 1
print(solution([1, 1, 9, 1, 1, 1], 0))  # 5



# any를 이용한 다른 풀이

# def solution(priorities, location):
#     queue =  [(i,p) for i,p in enumerate(priorities)]
#     answer = 0
#     while True:
#         cur = queue.pop(0)
#         if any(cur[1] < q[1] for q in queue):
#             queue.append(cur)
#         else:
#             answer += 1
#             if cur[0] == location:
#                 return answer
