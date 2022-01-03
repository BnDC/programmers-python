import math
import time


def solution(n):
    answer = [1] * (n + 1)
    x = int(math.sqrt(n))

    answer[0] = 0
    answer[1] = 0

    for i in range(2, x+1):
        for j in range(i*2, n+1, i):
            if answer[j] == 0:
                continue

            answer[j] = 0

    return answer.count(1)


start = time.time()
print(solution(1000000))
end = time.time()
print(end - start)

print(solution(5))
