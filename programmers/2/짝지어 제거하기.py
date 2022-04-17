def solution(s):
    answer = 1
    stack = []
    for word in s:
        if not stack:
            stack.append(word)
        elif stack[-1] == word:
            stack.pop()
        else:
            stack.append(word)
    
    if stack:
        answer = 0
    else:
        answer = 1

    return answer

print(solution('baabaa'))  # 1
print(solution('cdcd'))  # 0