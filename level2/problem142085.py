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


print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]) == 5)
print(solution(2, 4, [3, 3, 3, 3]) == 4)
