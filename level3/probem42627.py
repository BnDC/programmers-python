import heapq


def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    heap = []

    n = len(jobs)
    while i < n:
        for s, e in jobs:
            if start < s <= now:
                heapq.heappush(heap, [e, s])
        if len(heap) <= 0:
            now += 1
        else:
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            answer += now - cur[1]
            i += 1
    return answer // n


print(solution([[0, 3], [1, 9], [2, 6]]) == 9)