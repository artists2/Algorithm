count = 0
def solution(word):
    answer = 0
    def dfs(w, cnt):
        print(word, w)
        global count
        if word == w:
            return True
        if cnt == 5:
            return False
        
        count += 1
        if dfs(w + 'A', cnt + 1):
            return True
        count += 1
        if dfs(w + 'E', cnt + 1):
            return True
        count += 1
        if dfs(w + 'I', cnt + 1):
            return True
        count += 1
        if dfs(w + 'O', cnt + 1):
            return True
        count += 1
        if dfs(w + 'U', cnt + 1):
            return True
        return False

        
    dfs('', 0)
    answer = count
    return answer

print(solution("AAAAE"))  # 6
# print(solution("AAAE"))  # 10
# print(solution("I"))  # 1563
# print(solution("EIO"))  # 1189