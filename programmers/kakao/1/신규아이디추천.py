def solution(new_id):
    answer = ''
    new_id = new_id.lower() # 1
    white_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y',
                  'z','0','1','2','3','4','5','6','7','8','9',
                  '-','_','.']
    
    answer2 = ''
    for i in range(0, len(new_id)): # 2
        if new_id[i] in white_list:
            answer2 += new_id[i]
        else:
            continue
    print(answer2)
            
    answer3 = ''      
    for i in range(0, len(answer2)): # 3
        try:
            if answer2[i] == '.' and answer2[i+1] == '.':
                continue
            else:
                answer3 += answer2[i]
        except:
            if answer2[i] == '.':
                answer3 += answer2[i]
            break
    print(answer3)
    
    
    answer4 = '' 
    if answer3[0] == '.' and len(answer3) > 1: # 4
        answer4 = answer3[1:]
    else:
        answer4 = answer3
    if answer4[-1] == '.':
        answer4 = answer4[:-1]
    print(answer4)
    
    answer5 = '' 
    if answer4 == '': # 5
        answer5 += 'a'
    else:
        answer5 += answer4
    print(answer5)
    
    answer6 = ''
    if len(answer5) >= 16: # 6
        answer6 = answer5[0:15]
        if answer6[-1] == '.':
            answer6 = answer6[:-1]
    else:
        answer6 = answer5
    print(answer6)
    
    answer7 = ''
    if len(answer6) <= 2: # 7
        while len(answer6) < 3:
            answer6 += answer6[-1]
    answer7 = answer6
    
    
    answer = answer7
    return answer