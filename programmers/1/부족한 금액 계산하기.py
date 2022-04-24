def solution(price, money, count):
    answer = 0
    result = 0
    PRICE = price
    for i in range(2, count+2):
        result += price
        price = (PRICE * i)
    
    if result > money:
        answer = result - money

        
    return answer


print(solution(3, 20, 4))  # 10