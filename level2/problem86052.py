def move(r, c, d, directions):
    dr, dc = directions[d]
    return (r + dr) % n, (c + dc) % m


def rotate(d, direction):
    if direction == "R":
        return (d + 1) % 4
    elif direction == "L":
        return (d + 3) % 4
    return d


def solution(grid):
    global n, m
    directions = [
        [1, 0],
        [0, -1],
        [-1, 0],
        [0, 1]
    ]

    n = len(grid)
    m = len(grid[0])
    visited = [[[False] * 4 for _ in range(m)] for _ in range(n)]

    answer = []
    for r in range(n):
        for c in range(m):
            for d in range(4):
                if not visited[r][c][d]:
                    nr, nc, nd = r, c, d
                    cnt = 0
                    while not visited[nr][nc][nd]:
                        visited[nr][nc][nd] = True
                        cnt += 1
                        nr, nc = move(nr, nc, nd, directions)
                        nd = rotate(nd, grid[nr][nc])
                    answer.append(cnt)
    return sorted(answer)


print(solution(["SL", "LR"]) == [16])
print(solution(["S"]) == [1, 1, 1, 1])
print(solution(["R", "R"]) == [4, 4])
