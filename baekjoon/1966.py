# 프린터 큐 10:00
from collections import deque
T = int(input())

result = []

def solution():
    count = 0
    N, target = map(int, input().split())
    important = list(map(int, input().split(' ')))
    important[target] = str(important[target])
    importants = deque(important)


    while importants:
        flag = False
        element = importants.popleft()
        # if not importants:
        #     result.append(count)
        
        for i in importants:
            if int(i) > int(element):
                flag = True
                break
            else:
                continue
        
        if flag:
            importants.append(element)
            continue
        else:
            count += 1
            if type(element) == str:
                result.append(count)
                break
            else:
                continue
            



for _ in range(T):
    solution()

for s in result:
    print(s)