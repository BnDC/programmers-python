import collections
import sys

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    answer = sys.maxsize
    visited = [[0] * m for _ in range(n)]
    queue = collections.deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft();

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

    return -1 if visited[n - 1][m - 1] == 1 else visited[n - 1][m - 1] + 1

print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))