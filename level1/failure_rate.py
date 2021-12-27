def solution(N, stages):
    users = len(stages)
    failure_rate_list = []

    for stage in range(1, N+1):
        if users <= 0:
            users = 1
        failure_users = stages.count(stage)
        failure_rate_list.append((stage, failure_users / users))
        users -= failure_users

    failure_rate_list.sort(key=lambda x: -x[1])
    answer = [failure_rate[0] for failure_rate in failure_rate_list]

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
