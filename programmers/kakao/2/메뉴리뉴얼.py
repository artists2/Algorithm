from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    sort_orders = []
    
    for i in orders: # sort
        sort_orders.append(''.join(sorted(i)))

    for _course in course:
        tmp = []
        for order in sort_orders:
            for comb in combinations(order, _course):
                tmp.append(''.join(comb))
                
        _counter = Counter(tmp).most_common()
        
        for i, j in _counter:
            if _counter[0][1] == j and j >= 2:
                answer.append(i)

        answer.sort()
    return answer

    # 연속된 문자열도 나눌수 있음 combinations로. Counter과 most_common()활용법 이해하기