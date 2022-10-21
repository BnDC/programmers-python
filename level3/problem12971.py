def solution(sticker):
    n = len(sticker)
    if n == 1: return sticker[-1]
    return max(get_max(n - 1, sticker[1:]), get_max(n - 1, sticker[:-1]))


def get_max(n, arr):
    if n <= 2: return max(arr)
    dp = [0 for _ in range(n)]
    dp[0], dp[1] = arr[0], arr[1]
    for i in range(2, n):
        dp[i] = max(arr[i] + dp[i - 2], dp[i - 1])
    return dp[n - 1]


print(solution([14, 6, 5, 11, 3, 9, 2, 10]) == 36)
print(solution([1, 3, 2, 5, 4]) == 8)
