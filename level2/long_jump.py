def solution(n):
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1
    for i in range(n + 1):
        if i + 2 <= n:
            dp[i + 2] += dp[i]
        if i + 1 <= n:
            dp[i + 1] += dp[i]
    return dp[n] % 1234567


print(solution(4))
print(solution(3))
