# AC
from collections import deque

T = int(input())

result = []

def solution():
    p = input().replace("RR", "")
    n = int(input())
    p = list(p)

    if not n:
        lst = list(input())
        lst = []
        lst = deque(lst)

    if n:
        lst = map(int, input()[1:-1].split(','))
        lst = deque(lst)
        
    r = 0

    for f in p:
        if f == "R":
            r += 1
        elif f == "D":
            if not lst:
                result.append("error")
                return
            else:
                if r % 2 == 0:
                    lst.popleft()
                else:
                    lst.pop()
    
    lst = list(lst)
    if r % 2 == 0:
        result.append(str(lst).replace(' ',''))
    else:
        lst.reverse()
        result.append(str(lst).replace(' ',''))

    
for _ in range(T):
    solution()

for r in result:
    print(r)