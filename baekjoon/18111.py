from collections import Counter


def make_land(height):
    sec = 0
    for key in land:  # dic for문 (key 가ㅁ 나옴)
        print(key, height)
        if key < height:  # land높이가  쌓으려는 높이보다 작다면 -> 블록쌓기
            sec += (height - key) * land[key]
        elif key > height:  # land높이가 쌓으려는 높이보다 크다면 -> 블록 빼기
            sec += (key - height) * 2 * land[key]  # 시간 += (land높이 - 쌓으려는 높이) * 2 * land 높이의 개수
    return sec


N, M, B = map(int, input().split())
land = []
for _ in range(N):
    land += map(int, input().split())

print(land)

sum_land, size = sum(land), N * M
land = dict(Counter(land))
print(land)
h, min_sec = 0, 100000000000000

for i in range(257):
    print(i)
    if size * i <= sum_land + B:  # i높이로 만들기 위한 필요한 벽돌 개수     <= 벽돌의 총 개수
        sec = make_land(i)  # 땅고르기
        if sec <= min_sec:  # 시간 <= 최소 시간
            min_sec = sec  # 최소시간 업데이트
            h = i  # 높이 업데이트

print(min_sec, h)
