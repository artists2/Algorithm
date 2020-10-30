moneyList = []

moneyListLen = int(input())

for i in range(0, int(moneyListLen)):
    tmp = int(input())
    if tmp == 0:
        moneyList.pop()
    else:
        moneyList.append(tmp)
sumMoneyList = sum(moneyList)

print(sumMoneyList)

