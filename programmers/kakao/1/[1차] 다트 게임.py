def solution(dartResult):
    answer = []
    n = 0
    flag = False
    for i in range(0, len(dartResult)):
        if dartResult[i].isdigit():
            if flag and dartResult[i] == '0':
                flag = False
                continue
            if dartResult[i] == '1' and dartResult[i+1] == '0':
                answer.append(n)
                n = 10
                flag = True
                continue
            answer.append(n)
            n = int(dartResult[i])
        if dartResult[i] == 'S':
            n = n ** 1
        if dartResult[i] == 'D':
            n = n ** 2
        if dartResult[i] == 'T':
            n = n ** 3
        if dartResult[i] == '*':
            if answer:
                answer[-1] *= 2
            n *= 2
        if dartResult[i] == '#':
            n *= -1
    answer.append(n)
    return sum(answer)

print(solution('1S2D*3T'))  # 37


print(solution('1D2S#10S'))  # 9



print(solution('1D2S0T'))  # 3
print(solution('1S*2T*3S'))  # 23
print(solution('1D#2S*3S'))  # 5
print(solution('1T2D3D#'))  # -4
print(solution('1D2S3T*'))  # 59
print(solution('10S10S10S'))  # 30
