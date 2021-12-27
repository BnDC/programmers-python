def solution(N, stages):
    answer = []
    # users_number = len(stages)
    failure_rate_list = []
    previous_stage_failure_users = 0

    for failure_stage in range(1, N+1):

        previous_stage_failure_users = stages.count(failure_stage - 1)
        current_failure_users = stages.count(failure_stage)

        failure_rate = current_failure_users / \
            (N - previous_stage_failure_users)
        failure_rate_list.append(failure_rate)

    for _ in range(len(failure_rate_list)):
        max_failure_rate_index = failure_rate_list.index(
            max(failure_rate_list))
        answer.append(max_failure_rate_index + 1)
        failure_rate_list[max_failure_rate_index] = -1

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
