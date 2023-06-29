import heapq


def solution(n, k, enemy):
    answer, length = 0, len(enemy)
    heap = []

    for i in range(length):
        heapq.heappush(heap, -enemy[i])
        n -= enemy[i]

        if n < 0:
            if k <= 0:
                break
            k -= 1
            n += -heapq.heappop(heap)
        answer += 1
    return answer
