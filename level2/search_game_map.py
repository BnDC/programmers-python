import sys

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    result = 1
    answer = sys.maxsize

    def dfs(x, y):
        nonlocal result, answer
        if x == n - 1 and y == m - 1:
            answer = min(answer, result)
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                result += 1
                maps[x][y] = 0
                dfs(nx, ny)
                result -= 1
                maps[x][y] = 1

    dfs(0, 0)

    return -1 if answer == sys.maxsize else answer