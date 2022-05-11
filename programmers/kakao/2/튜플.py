import copy 

def solution(s):
    answer = []
    t = []
    temp_string = ''
    temp_set = set()

    for string in s[1:-1]:
        if string.isdigit():
            temp_string += string
        if string == ',':
            if temp_string:
                temp_set.add(temp_string)
                temp_string = ''
        if string == '}':
            if temp_string:
                temp_set.add(temp_string)
                temp_string = ''
            if temp_set:
                t.append(temp_set)
                temp_set = set()
    t.sort(key=len, reverse=True)

    for i in range(0, len(t)-1):
        answer.append(int(list(t[i] - t[i+1])[0]))
    answer.append(int(list(t[-1])[0]))
    answer.reverse()    

    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))  # [2, 1, 3, 4]
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))  # [2, 1, 3, 4]
print(solution("{{20,111},{111}}"))  # [111, 20]
print(solution("{{123}}"))  # [123]
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))  # [3, 2, 4, 1]