def convert(n):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, 3)
        rev_base += str(mod)

    return int(str(rev_base[::-1])[::-1], 3)


def solution(n):
    return convert(n)

print(solution(45))  # 7
print(solution(125))  # 229
