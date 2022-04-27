# 톱니바퀴
from collections import deque

wheels = []  # N = 0, S = 1

for _ in range(4):  # 0 ~ 3번째 바퀴
    wheels.append(list(map(int, input())))

N = int(input())
actions = []  # : (돌릴 바퀴 번호, 방향), 방향: 1 시계 -1 반시계

for i in range(N):
    (num, d) = map(int, input().split())
    actions.append((num-1, d))  # idx 랑 맞추기


def check_wheels(n, check: list, directions):  # recur
    check.append((n, directions))
    if n == 0:
        if wheels[n][2] != wheels[n+1][6]:
            if ((n+1), -directions) not in check:
                check_wheels(n+1, check, -directions)
        else:
            return check
    elif n == 3:
        if wheels[n][6] != wheels[n-1][2]:
            if ((n-1), -directions) not in check:
                check_wheels(n-1, check, -directions)
        else:
            return check
    else:  # 1, 2
        if wheels[n][6] != wheels[n-1][2]:
            if ((n-1), -directions) not in check:
                check_wheels(n-1, check, -directions)
        if wheels[n][2] != wheels[n+1][6]:
            if ((n+1), -directions) not in check:
                check_wheels(n+1, check, -directions)
        return check
    return check


def right_shift(e: list) -> list:
    e = deque(e)
    e.rotate(1)
    return list(e)


def left_shift(e: list) -> list:
    e =deque(e)
    e.rotate(-1)
    return list(e)


def operate_wheels(wheel_list):  # directions = 1시계 -1반시계(왼쪽)
    # [(2, 1), (1, -1), (0, 1)]
    for w in wheel_list:
        num, direction = w[0], w[1]
        if direction == 1:  # right_shift
            wheels[num] = right_shift(wheels[num])
        if direction == -1:  # left_shift
            wheels[num] = left_shift(wheels[num])


for action in actions:  # 동작코드
    wheel_num, direction = action[0], action[1]
    operate_wheels(check_wheels(wheel_num, [], direction))

print(wheels[0][0] * 1 + wheels[1][0] * 2 + wheels[2][0] * 4 + wheels[3][0] * 8)

