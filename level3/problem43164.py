import collections


def solution(tickets):
    answer = []
    graph = collections.defaultdict(list)

    for a, b in tickets:
        graph[a].append(b)
        graph[a].sort(reverse=True)

    stack = ["ICN"]
    while stack:
        cur = stack.pop()
        if len(graph[cur]) == 0:
            answer.append(cur)
        else:
            stack.append(cur)
            stack.append(graph[cur].pop())
    return answer[::-1]


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]) == ["ICN", "JFK", "HND", "IAD"])
print(
    solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]) == ["ICN", "ATL", "ICN",
                                                                                                   "SFO", "ATL", "SFO"]
)
