def solution(m, n, board):
    answer = 0
    maps = []


    # maps 좌표 만들기
    for i in range(0, m):
        tmp = []
        for j in range(0, n):
            tmp.append(board[i][j])
        maps.append(tmp)
    

    while True:
        rm = []
        # 지워질 블록 수집
        for x in range(0, m-1):
            for y in range(0, n-1):
                if maps[x][y] == maps[x+1][y] and maps[x][y+1] == maps[x+1][y+1] and maps[x][y] == maps[x+1][y+1] and maps[x][y] != 0:
                    rm.append((x, y))
                    rm.append((x+1, y))
                    rm.append((x, y+1))
                    rm.append((x+1, y+1))

        rm = set(rm)
        answer += len(rm)

        if not len(rm):
            return answer
        else: 
            # 지워질 블록 지우기
            for rmv in rm:
                maps[rmv[0]][rmv[1]] = 0
        
        # 지워진 칸 채우기
        while True:
            mv = 0
            for x in range(0, m-1):
                for y in range(0, n):
                    if maps[x+1][y] == 0 and maps[x][y]:  # 밑 칸이 비어있을 때
                        maps[x+1][y] = maps[x][y]
                        maps[x][y] = 0
                        mv = 1
                    else:  # 밑에 칸이 비어있지 않을 때
                        continue
            if mv == 0:
                break


        

    return answer


# print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
# print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
# print(solution(2,2,["aa","aa"]))
print(solution(7, 2, ["AA", "BB", "AA", "BB", "ZZ", "ZZ", "CC"]))