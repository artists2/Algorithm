#공주님의 정원
import sys
import heapq

N = int(input())
Y = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 1년의 총 일수 Y[0] = 1월

flowers = []

for _ in range(N):
    (sm, sd, em, ed) = map(int, sys.stdin.readline().split())
    flowers.append((sm, sd, em, ed))


print(flowers)
# flowers.sort(key= lambda x: (x[2], x[0], x[3], x[1])) # 끝 월, 시작 월, 끝 일, 시작 일 순으로 정렬
flowers.sort(key= lambda x: x[2])
print(flowers)

queue = []

heapq.heappush(queue, (3,1,3,1)) # 하루만 

flag_favorite_season = False

for i in range(0, N):
    if flag_favorite_season == False: # 공주님이 좋아하는 계절 검증
        if (flowers[i][0] >= 3) and (flowers[i][0] < 12):
            flag_favorite_season = True
    
print(flag_favorite_season)
