def solution(n):
    dp = [0 for _ in range(n + 1)]
    dp[2] = 3

    for i in range(4, n + 1, 2):
        if i % 2 == 0:
            dp[i] += dp[i - 2] * 3
            for j in range(4, n - 1, 2):
                dp[i] += dp[i - j] * 2
            dp[i] += 2

    return dp[n] % 1000_000_007

print(solution(16))