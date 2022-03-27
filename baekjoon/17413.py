# 단어 뒤집기 2

S = list(input())

stck = ""
result = ""

flag = 0
for s in S:
    if s == "<":
        result += stck[::-1]
        stck = ""
        flag = 1
        result += s
        continue
    if s == ">":
        flag = 0
        result += s 
        continue
    if s == " ":
        if flag:
            result += s
            continue
        else:
            result += stck[::-1]
            result += s
        stck = ""
        continue
    
    if flag:
        result += s
    else:
        stck += s
result += stck[::-1]
print(result)

