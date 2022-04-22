puzzle = [list(map(int,list(input()))) for _ in range(9)]
zero_location = [(i, j) for i in range(9) for j in range(9) if not puzzle[i][j]]

def search_square(r, c, v):
    r = r // 3 * 3
    c = c // 3 * 3
    for i in range(3):
        for j in range(3):
            if puzzle[r+i][c+j] == v:
                return False
    return True

def search_row(r, c, v):  # 행
    for i in range(9):
        if puzzle[r][i] == v:
            return False
    return True

def search_col(r, c, v):  # 
    for i in range(9):
        if puzzle[i][c] == v:
            return False
    return True

def run(depth):
    if depth == len(zero_location):
        return True
    r, c = zero_location[depth]
    for v in range(1, 10):
        if search_row(r, c, v) and search_col(r, c, v) and search_square(r, c, v):
            puzzle[r][c] = v
            if run(depth+1):
                return True
            puzzle[r][c] = 0


run(0)

for i in range(9):
    for j in range(9):
        print(puzzle[i][j], end="")
    print("")

