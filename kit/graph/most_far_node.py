import heapq


def solution(n, edge):
    answer = 0
    INF = int(1e9)
    distance = [INF] * (n + 1)
    distance[1] = 0
    graph = [[] for i in range(n + 1)]

    for v, u in edge:
        if v < u:
            graph[v].append((u, 1))
        else:
            graph[u].append((v, 1))

    heap = []

    heapq.heappush(heap, (0, 1))

    while heap:
        way_point_cost, v = heapq.heappop(heap)

        if distance[v] < way_point_cost:
            continue

        for u, cost in graph[v]:
            total_cost = cost + way_point_cost
            if total_cost < distance[u]:
                distance[u] = total_cost
                heapq.heappush(heap, (total_cost, u))

    for i in range(len(distance)):
        if distance[i] == INF:
            distance[i] = -1

    return distance.count(max(distance))