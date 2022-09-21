import collections


def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    reported_map = collections.defaultdict(set)

    for r in report:
        reporter, reported = r.split(" ")
        reported_map[reported].add(reporter)

    for key in reported_map.keys():
        if (len(reported_map[key])) >= k:
            for reporter in reported_map[key]:
                idx = id_list.index(reporter)
                answer[idx] += 1
    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi", "frodo", "apea"]))
