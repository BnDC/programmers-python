import itertools
import sys


def solution(n, weak, dist):
    answer = sys.maxsize
    length = len(weak)
    total_people = len(dist)

    circular_weak = weak[:]
    for i in range(length):
        circular_weak.append(n + weak[i])

    for start in range(length):
        for permutation in itertools.permutations(dist, total_people):
            index = 0
            cur = circular_weak[start]
            for i in range(start + 1, start + length):
                if circular_weak[i] - cur > permutation[index]:
                    index += 1
                    cur = circular_weak[i]

                if index >= total_people:
                    index = -1
                    break
            if index != -1:
                answer = min(answer, index + 1)
    return answer if answer != sys.maxsize else -1


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]) == 2)
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]) == 1)
