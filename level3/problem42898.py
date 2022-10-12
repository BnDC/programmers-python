def solution(m, n, puddles):
    _map = [[0] * (m + 1) for _ in range(n + 1)]
    _map[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1: continue
            if [j, i] in puddles:
                _map[i][j] = 0
            else:
                _map[i][j] = (_map[i - 1][j] + _map[i][j - 1]) % 1000_000_007
    return _map[n][m]


print(solution(4, 3, [[2, 2]]) == 4)
