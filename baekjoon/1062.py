# 가르침

from itertools import combinations

N, K = map(int, input().split())

if K < 5:
    print(0)
else:
    K -= 5
    elements = {'a', 'n', 't', 'i', 'c'}
    words = []
    count = 0

    dic = {ky: v for v, ky in enumerate(
        (set(map(chr, range(ord('a'), ord('z') + 1)))) - elements)}

    for _ in range(N):
        tmp = 0
        for c in set(input())-elements:
            tmp |= (1<<dic[c])

        words.append(tmp)
    
    bin2char = (2**i for i in range(21))  # 26(소문자 알파벳 총 개수) - 5(무조건 배워야하는 알파벳 antic 개수)
    
    print(bin2char)
    for combi in combinations(bin2char, K):
        temp = sum(combi)

        ct = 0
        for cb in words:
            if temp & cb == cb:
                ct += 1
        
        count = max(count, ct)
    print(count)
    print(dic, words)