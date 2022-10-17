import collections


def solution(A, B):
    A.sort()
    B.sort()
    n = len(A)
    answer = 0

    q = collections.deque(B)
    for i in range(n - 1, -1, -1):
        if len(q) == 0:
            break

        if q[-1] > A[i]:
            answer += 1
            q.pop()
        else:
            q.popleft()
    return answer


print(solution([5, 1, 3, 7], [2, 2, 6, 8]) == 3)
print(solution([2, 2, 2, 2], [1, 1, 1, 1]) == 0)
