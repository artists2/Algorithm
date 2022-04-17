def is_right_string(s):
    _stack = []
    for e in s:
        if e == "(":
            _stack.append(e)
        else:
            if _stack and _stack[-1] == "(":
                _stack.pop()
    
    if _stack:
        return False
    else:
        return True
        
    return



def solution(p):
    answer = ''

    if p == "":
        return ""
        
    stack = []
    u = ""
    v = ""

    for i in range(0, len(p)):
        u += p[i]
        if u.count("(") == u.count(")"):
            v = p[i+1:]
            break
    if is_right_string(u):
        return u + solution(v)
    if not is_right_string(u):
        ms = "("
        ms += solution(v)
        ms += ")"

        for i in u[1:-1]:
            if i == ")":
                ms += "("
            if i == "(":
                ms += ")"

        answer = ms

    return answer




# print(solution("(()())()"))
# print(solution(")("))
print(solution("()))((()"))



# for i in range(0, len(p)):
#         if p[i] == "(":
#             stack.append(p[i])
#             u += p[i]
#         else:
#             if stack and stack[-1] == "(":
#                 stack.pop()
#                 u += p[i]
#             else:
#                 u += p[i]
#                 pass
        
#         if not stack:
#             v += p[i+1:]
#             break
    
#     print(f"u = {u}, v = {v}")