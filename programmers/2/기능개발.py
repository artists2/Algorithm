def solution(progresses, speeds):
    answer = []
    daylst = []
    day = 0
    for i in range(0, len(progresses)):
        day = (100 - progresses[i]) // speeds[i]
        if (100 - progresses[i]) % speeds[i]:
            day += 1
        daylst.append(day)
    i = 0
    j = 1
    while j < len(daylst):
        if daylst[i] >= daylst[j]:
            if j == len(daylst)-1:
                answer.append(j-i+1)
            j += 1
        else:
            if daylst[i] < daylst[j]:
                answer.append(j-i)
                if j == len(daylst)-1:
                    answer.append(1)
                i = j
                j += 1
    return answer