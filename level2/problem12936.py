import math


def solution(n, k):
    candidates = list(range(1, n + 1))
    answer = []
    while n != 0:
        fac = math.factorial(n - 1)
        p, k = (k - 1) // fac, k % fac
        answer.append(candidates[p])
        del candidates[p]
        n -= 1
    return answer


print(solution(5, 100) == [5, 1, 3, 4, 2])
print(solution(3, 5) == [3, 1, 2])
