import sys


def solution(matrix_sizes):
    n = len(matrix_sizes)
    INF = sys.maxsize
    dp = [[INF] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0

    for term in range(1, n):
        for start in range(n - term):
            end = start + term
            for k in range(start, end):
                dp[start][end] = min(
                    dp[start][end],
                    dp[start][k] + dp[k + 1][end]
                    + matrix_sizes[start][0] * matrix_sizes[k][1] * matrix_sizes[end][1]
                )
    return dp[0][n - 1]


print(solution([[5, 3], [3, 10], [10, 6]]) == 270)
