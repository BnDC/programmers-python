import heapq


def solution(n, works):
    if sum(works) <= n:
        return 0

    heap = [-work for work in works]
    heapq.heapify(heap)

    while n != 0:
        heapq.heappush(heap, heapq.heappop(heap) + 1)
        n -= 1

    return sum(i ** 2 for i in heap)
