import collections


def solution(clothes):
    answer = 1
    stuff = collections.defaultdict(list)

    for name, kind in clothes:
        stuff[kind] += [name]

    for s in stuff.values():
        answer *= len(s) + 1

    answer -= 1

    return answer


print(solution([["yellowhat", "headgear"], [
      "bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], [
      "bluesunglasses", "face"], ["smoky_makeup", "face"]]))
