def solution(str1, str2):
    answer = 0
    string1 = []
    string2 = []
    for i in range(0, len(str1)-1):
        if str1[i:i+2].isalpha():
            string1.append(str1[i:i+2].lower())
    for i in range(0, len(str2)-1):
        if str2[i:i+2].isalpha():
            string2.append(str2[i:i+2].lower())
    
    if (not string1) and (not string2):
        return 65536

    # 다중집합 합집합
    temp = string1.copy()
    result = string1.copy()

    for i in string2:
        if i not in temp:
            result.append(i)
        else:
            temp.remove(i)
    A = len(result)

    # 다중집합 교집합
    temp = string1.copy()
    result = []

    for i in string2:
        if i in temp:
            temp.remove(i)
            result.append(i)
        
    B = len(result)

    answer = int((B/A) * 65536)

    return answer

print(solution("FRANCE", "french"))  # 16384
print(solution("handshake", "shake hands"))  # 65536
print(solution("aa1+aa2", "AAAA12"))  # 43690
print(solution("E=M*C^2", "e=m*c^2"))  # 65536