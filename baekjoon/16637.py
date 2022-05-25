N = int(input())
INF = -10e9
num, op = [], []
max_number = INF

for string in input():
    if string.isdigit():
        num.append(int(string))
    else:
        op.append(string)


def calc(num1, num2, sign):
    if sign == '+':
        return num1 + num2
    if sign == '-':
        return num1 - num2
    if sign == '*':
        return num1 * num2


def solve(idx, res):
    global max_number

    if idx >= len(op):
        max_number = max(max_number, res)
        return

    solve(idx+1, calc(res, num[idx+1], op[idx]))

    if idx+1 < len(op):
        solve(idx+2, calc(res, calc(num[idx+1], num[idx+2], op[idx+1]), op[idx]))


solve(0, num[0])

print(max_number)
