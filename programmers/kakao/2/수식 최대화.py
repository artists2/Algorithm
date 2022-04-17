from itertools import permutations
import copy

def cal(a, b, sym):
    if sym == "+":
        return str(int(a) + int(b))
    if sym == "-":
        return str(int(a) - int(b))
    if sym == "*":
        return str(int(a) * int(b))
    return

def solution(expression):
    answer = []
    stack = []
    tmp = ''
    for e in expression:
        if e.isdigit():
            tmp += e
        else:
            stack.append(tmp)
            stack.append(e)
            tmp = ''
    stack.append(tmp)
    copy_stack = copy.deepcopy(stack)
    for p in permutations(["+", "-", "*"], 3):
        stack = copy.deepcopy(copy_stack)
        print(p, '------------')
        for pp in p:
            stck = []
            while len(stack) != 0:
                e = stack.pop(0)
                if e == pp:
                    stck.append(cal(stck.pop(), stack.pop(0), e))
                else:
                    stck.append(e)
                print(stack, stck)
            stack = stck[:]
        answer.append(abs(int(stck[0])))
                

    return max(answer)


print(solution("100-200*300-500+20"))  # 60420
# print(solution("50*6-3*2"))  # 300

# ["+", "-", "*"] []