def solution(s):
    answer = len(s)  # 줄이지 않았을 때

    for i in range(1, len(s)//2 + 1):
        res = ''
        count = 1
        tmp = s[:i]  # 글자수 만큼 슬라이싱

        for j in range(i, len(s)+ i, i):  # 슬라이싱 된 단어 뒤로부터 슬라이싱 된 단어의 개수만큼 간격두어서 써치
            if s[j:j+i] == tmp:  # 동일하면
                count += 1
            else:
                if count == 1:  # 겹치는게 없을 때
                    res += tmp
                else:
                    res += str(count) + tmp
                tmp = s[j:j+i]
                count = 1
        answer = min(answer, len(res))

    return answer

print(solution('abcabcabcabcdededededede'))