def solution(n):
    answer = []

    def dfs(n, start, mid, end):
        if n == 1:
            answer.append([start, end])
            return
        dfs(n - 1, start, end, mid)
        dfs(1, start, mid, end)
        dfs(n - 1, mid, start, end)
        return

    dfs(n, 1, 2, 3)
    return answer


print(solution(2) == [[1, 2], [1, 3], [2, 3]])
