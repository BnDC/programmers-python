import math


def solution(n, stations, w):
    answer = 0
    cur = 1
    diameter = 2 * w + 1

    for s in stations:
        answer += max(math.ceil((s - w - cur) / diameter), 0)
        cur = s + w + 1
    if n >= cur:
        answer += max(math.ceil((n - cur + 1) / diameter), 0)
    return answer


print(solution(11, [4, 11], 1) == 3)
print(solution(16, [9], 2) == 3)
