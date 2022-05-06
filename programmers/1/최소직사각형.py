
def solution(sizes):
    answer = 0
    w = []
    h = []
    for size in sizes:
        a, b = size
        if a >= b:
            w.append(a)
            h.append(b)
        else:
            w.append(b)
            h.append(a)
    
    print(w, h)
    print(max(w)*max(h))

    return answer




# def solution(sizes):
#     answer = max(max(size) for size in sizes) * max(min(size) for size in sizes)

#     return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))  # 4000
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))  # 120
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))  # 133