from collections import deque

def is_correct(s) -> bool:
    stack = []
    for _str in s:
        if _str == '{' or _str == '(' or _str == '[':
            stack.append(_str)
        else:
            if not stack:
                return False
            else:
                if _str == '}' and stack[-1] == '{':
                    stack.pop()
                    continue
                if _str == ']' and stack[-1] == '[':
                    stack.pop()
                    continue
                if _str == ')' and stack[-1] == '(':
                    stack.pop()
                    continue
                else:
                    return False
    if stack:
        return False
    return True

def solution(s):
    answer = 0
    n = len(s) - 1
    
    for i in range(n):
        if is_correct(s):
            answer += 1
        
        s = deque(s)
        s.rotate(-1)    
    
    return answer