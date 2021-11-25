#강의실 배정
import heapq
import sys

N = int(input()) # N개의 수업
classes = [list(map(int,sys.stdin.readline().split())) for _ in range(N)] # 입력방식에 대한 차이

# 시간초과 나는 입력 코드
# classes = []
# for _ in range(0, N):
#     (S, T) = map(int, input().split())
#     classes.append((S, T))

classes.sort(key= lambda x: (x[0])) # 회의 시작시간으로 정렬

heaps = []
heapq.heappush(heaps, classes[0][1])


for j in range(1, N):
    if heaps[0] > classes[j][0]:
        heapq.heappush(heaps, classes[j][1])
    else:
        heapq.heappop(heaps)
        heapq.heappush(heaps, classes[j][1])

print(len(heaps))


# for i, j in classes: # i = S, j =T
#     if heaps[0] <= i: # 끝나는 시간보다 시작시간이 커서 강의실을 똑같이 사용 가능하면
#         heapq.heappop(heaps)
#         heapq.heappush(heaps, j)
#     else: # 끝나는 시간보다 시작시간이 작으면 
#         heapq.heappush(heaps, j)


# 7
# 17 19 
# 17 20
# 17 21
# 17 22
# 1 3
# 2 4
# 3 5
# -> 결과 값 4