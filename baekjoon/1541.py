lst = input().split('-')
temp = []
tmp = []

for i in lst:
    temp.append(i.split('+'))

for i in range(0, len(temp)):
    temp[i] = list(map(int, temp[i]))
    tmp.append(sum(temp[i]))

for i in range(1, len(tmp)):
    tmp[0] -= tmp[i]

result = tmp[0]

print(result)

# 최솟값을 만들기 위해서는 - 기준으로 괄호를 치면 된다.
# 예를 들어
# 55 - 50 + 40 - 30 + 20
# 위와 같이 입력을 받았을때 - 기준으로
# 55 - (50 + 40) - (30 + 20)
# 이렇게 괄호를 쳤을때 최솟값이 된다.
# 그래서 입력을 받을때 - 기준으로 입력을 받아준다.
# 위와 같이 입력을 받았을때
# ['55', '50 + 40', '30 + 20']
# 이렇게 입력을 받게 되는데
# 각 원소에 있는 숫자들을 계산해주고
# 맨 처음의 원소는 더해주고 나머지는 빼준다. (?)
# 55-50+40-30+20
# 00009-00009
