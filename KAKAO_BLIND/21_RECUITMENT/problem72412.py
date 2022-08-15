import collections
import bisect


def solution(info, query):
    search_dict = collections.defaultdict(list)
    answer = []

    def dfs(idx, result, keys, value):
        if len(result) == 4:
            search_dict[tuple(result)].append(value)
            return
        dfs(idx + 1, result + [keys[idx]], keys, value)
        dfs(idx + 1, result + ["-"], keys, value)
        return

    for person in info:
        key_candidates = person.split(" ")

        value = int(key_candidates[-1])
        key_candidates = key_candidates[:-1]
        dfs(0, [], key_candidates, value)

    for key in search_dict.keys():
        search_dict[key].sort()

    for q in query:
        language, duty, career, food_and_score = q.split(" and ")
        food, value = food_and_score.split(" ")
        value = int(value)
        search_key = (language, duty, career, food)

        cnt = bisect.bisect_left(search_dict[search_key], value)
        answer.append(len(search_dict[search_key]) - cnt)

    return answer


info = [
    "java backend junior pizza 150",
    "python frontend senior chicken 210",
    "python frontend senior chicken 150",
    "cpp backend senior pizza 260",
    "java backend junior chicken 80",
    "python backend senior chicken 50"
]

query = [
    "java and backend and junior and pizza 100",
    "python and frontend and senior and chicken 200",
    "cpp and - and senior and pizza 250",
    "- and backend and senior and - 150",
    "- and - and - and chicken 100",
    "- and - and - and - 150"
]

print(solution(info, query) == [1, 1, 1, 1, 2, 4])
