def solution(N, stages):
    answer = []
    users = len(stages)
    failure_rate_list = []
    #failure_users = [stages.count(stage) for stage in range(1, N+1)]
    #answer = [failure_users[i] / (users - failure_users[i-1]) for i in range(len(failure_users))]

    for stage in range(1, N+1):
        failure_rate = stages.count(stage) / users
        failure_rate_list.append(failure_rate)
        users -= stages.count(stage)

    for _ in range(len(failure_rate_list)):
        index = failure_rate_list.index(max(failure_rate_list))
        failure_rate_list[index] = -1
        answer.append(index + 1)

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
