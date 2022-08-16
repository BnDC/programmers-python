import sys


def solution(n, s, a, b, fares):
    dist = [[sys.maxsize] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dist[i][i] = 0
    for x, y, c in fares:
        dist[x][y] = c
        dist[y][x] = c

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    answer = min(dist[s][b] + dist[s][a], dist[s][a] + dist[a][b], dist[s][b] + dist[b][a])

    for i in range(n + 1):
        answer = min(answer, dist[s][i] + dist[i][a] + dist[i][b])

    return answer


print(
    solution(6, 4, 6, 2, [
        [4, 1, 10], [3, 5, 24], [5, 6, 2],
        [3, 1, 41], [5, 1, 24], [4, 6, 50],
        [2, 4, 66], [2, 3, 22], [1, 6, 25]])
    == 82)
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]) == 14)
print(solution(6, 4, 5, 6,
               [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]) == 18)
