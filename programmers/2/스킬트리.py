def solution(skill, skill_trees):
    answer = len(skill_trees)
    skill_tmp = ''
    skill_lst = [skill[i] for i in range(0, len(skill))]      
 
    for i in range(0, len(skill_trees)):
        for j in range(0, len(skill_trees[i])):
            for k in range(0, len(skill_lst)):
                if skill_trees[i][j] == skill_lst[k]:
                    skill_tmp += skill_lst[k]
        print(skill_tmp)
 
        if len(skill_tmp) == 0:
            pass
            #answer -= 1
        else:
            for i in range(0, len(skill)):
                try:
                    print(skill[i],skill_tmp[i])
                    if skill[i] != skill_tmp[i]:
                        answer -= 1
                        break
                    else:
                        continue
                except:
                    break
 
        skill_tmp = ''
 
    return answer


# 선행스킬중 아무스킬도 배우지 않았을 때를 "가능하지 않은 경우의 수"로 처리를 해서 애를 좀 먹었다.. 

# code 13 - 15 부분..

