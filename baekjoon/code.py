from collections import Counter


def make_land(height):
    sec = 0
    for key in land:
        print(key, height)
        if key < height:
            sec += (height - key) * land[key]
        elif key > height:
            sec += (key - height) * 2 * land[key]
    return sec


n, m, inven = map(int, input().split())
land = []
for _ in range(n):
    land += map(int, input().split())

_sum, _len = sum(land), n * m
land = dict(Counter(land))
height, min_sec = 0, 100000000000000
print(land)
for i in range(257):
    print()
    print(i)
    if _len * i <= _sum + inven:
        sec = make_land(i)
        print(sec)
        if sec <= min_sec:
            min_sec = sec
            height = i

print(min_sec, height)
