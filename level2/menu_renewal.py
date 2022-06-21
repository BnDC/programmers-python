import collections
from itertools import combinations


def solution(orders, course) -> list:
    def generate_combination(s: str):
        for i in range(2, len(s) + 1):
            for com in combinations(s, i):
                candi = ''.join(sorted(list(com)))
                if len(candi) > 1 and len(candi) in course:
                    len_list[len(candi)][candi] += 1
    answer = []
    len_list = [collections.defaultdict(int) for _ in range(10 + 1)]

    for i in range(len(orders)):
        generate_combination(orders[i])

    for c in course:
        max_ = max(len_list[c].values())
        for key in len_list[c].keys():
            if max_ > 1 and len_list[c][key] == max_:
                answer.append(key)
    answer.sort()

    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))