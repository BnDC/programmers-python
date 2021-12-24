from itertools import combinations


def solution(nums):
    n = len(nums)//2
    com = set(combinations(nums, n))
    count = set(map(lambda x: len(set(x)), com))

    return max(count)
