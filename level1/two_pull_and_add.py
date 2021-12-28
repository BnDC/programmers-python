from itertools import combinations


def solution(numbers):
    answer = set()
    com = list(combinations(numbers, 2))

    for e in com:
        answer.add(sum(e))
    answer = list(answer)
    answer.sort()

    return answer


print(solution([2, 1, 3, 4, 1]))
