def solution(triangle):
    triangle = [[0] + _ + [0] for _ in triangle]

    for i in range(1, len(triangle)):
        for j in range(1, i+2):
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    return max(triangle[-1])