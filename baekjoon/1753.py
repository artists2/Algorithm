# 최단경로
import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

V, E = map(int, input().split())

start = int(input())

distances = [INF] * (V + 1)

graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w)) # u -> v 의 비용이 w

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    
    distances[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distances[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distances[i[0]]:
                distances[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, V + 1):
    if distances[i] == INF:
        print("INF")
    else:
        print(distances[i])