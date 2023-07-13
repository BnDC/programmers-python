def solution(sequence):
    answer = 0
    length = len(sequence)

    if length == 1:
        return abs(sequence[0])

    dp = [[0, 0] for _ in range(length)]

    for i in range(length):
        if i % 2 == 0:
            dp[i][0] = sequence[i] * -1
            dp[i][1] = sequence[i]
        else:
            dp[i][0] = sequence[i]
            dp[i][1] = sequence[i] * -1

    for i in range(1, length):
        dp[i][0] = max(dp[i][0], dp[i][0] + dp[i - 1][0])
        dp[i][1] = max(dp[i][1], dp[i][1] + dp[i - 1][1])
        answer = max(answer, dp[i][0], dp[i][1])

    return answer


print(solution([2, 3, -6, 1, 3, -1, 2, 4]) == 10)