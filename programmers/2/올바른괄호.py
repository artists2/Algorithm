def solution(s):
    lst =[]
    if s.count('(') == s.count(')') and s[0] == '(' and s[-1] == ')':
        for i in range(0, len(s)):
            if s[i] == '(':
                lst.append('(')
            elif s[i] == ')':
                try:
                    lst.pop()
                except:
                    print('except')
                    return False
    else:
        return False
    return True
