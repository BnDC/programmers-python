import heapq


def solution(N, road, K):
    answer = 0
    INF = int(1e9)

    dist = [INF] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    heap = []

    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    heapq.heappush(heap, (1, 0))
    dist[1] = 0
    dist[0] = 0

    while heap:
        v, acc = heapq.heappop(heap)

        if dist[v] < acc:
            continue

        for u, cost in graph[v]:
            if dist[u] > acc + cost:
                dist[u] = acc + cost
                print(u, dist)
                heapq.heappush(heap, (u, acc + cost))

    for i in range(1, len(dist)):
        if dist[i] <= K:
            answer += 1

    return answer