def solution(alp, cop, problems):
    alp_max = 0
    cop_max = 0

    n = len(problems)
    INF = float('inf')

    for i in range(n):
        alp_max = max(alp_max, problems[i][0])
        cop_max = max(cop_max, problems[i][1])

    alp_max = max(alp_max, alp)
    cop_max = max(cop_max, cop)

    dp = [
        [INF] * (cop_max + 1)
        for _ in range(alp_max + 1)
    ]
    dp[alp][cop] = 0

    problems.append([0, 0, 0, 1, 1])
    problems.append([0, 0, 1, 0, 1])

    for i in range(alp, alp_max + 1):
        for j in range(cop, cop_max + 1):
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if alp_req <= i and cop_req <= j \
                        and dp[i][j] != INF:
                    target_alp, target_cop = min(i + alp_rwd, alp_max), min(j + cop_rwd, cop_max)
                    dp[target_alp][target_cop] = min(dp[target_alp][target_cop], dp[i][j] + cost)

    return dp[alp_max][cop_max]


print(solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]) == 15)
print(solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]) == 13)
