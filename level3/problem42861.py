import heapq


def find(a, parent):
    if a != parent[a]:
        parent[a] = find(parent[a], parent)
    return parent[a]


def union(a, b, parent):
    pa = find(a, parent)
    pb = find(b, parent)

    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb


def solution(n, costs):
    answer = 0
    heap = []
    parent = [i for i in range(n + 1)]

    for a, b, cost in costs:
        heapq.heappush(heap, (cost, a, b))

    while heap:
        cost, a, b = heapq.heappop(heap)
        if find(a, parent) != find(b, parent):
            union(a, b, parent)
            answer += cost
    return answer


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]) == 4)