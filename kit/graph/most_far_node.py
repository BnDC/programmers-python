import heapq


def solution(n, edge):
    INF = int(1e9)
    answer = 0
    graph = [[] for _ in range(n + 1)]
    visited = [True]
    distance = [INF] * (n + 1)
    distance[1] = 0

    for u, v in edge:
        # if u < v:
        graph[u].append((1, v))
        # else:
        graph[v].append((1, u))

    heap = []
    heapq.heappush(heap, (0, 1))

    while heap:
        initial_cost, v = heapq.heappop(heap)

        # if distance[way_point] < initial_cost:
        # print(1)

        for cost, u in graph[v]:
            total_cost = initial_cost + cost
            if total_cost < distance[u]:
                distance[u] = total_cost
                heapq.heappush(heap, (total_cost, u))

    for i in range(len(distance)):
        if distance[i] == INF:
            distance[i] = -1

    answer = distance.count(max(distance))

    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))