directions = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0]
]
n = 5


def simulate(place):
    answer = 1
    visited = [[0] * n for _ in range(n)]

    def dfs(x, y, depth, place):
        nonlocal answer
        if answer == 0:
            return

        if depth >= 2:
            return

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and place[nx][ny] != "X":
                if place[nx][ny] == "P":
                    answer = 0
                    return
                visited[x][y] = 1
                dfs(nx, ny, depth + 1, place)
        return

    for i in range(n):
        for j in range(n):
            if place[i][j] == 'P':
                dfs(i, j, 0, place)

    return answer


def solution(places):
    answer = []

    for place in places:
        result = simulate(place)
        answer.append(result)

    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP",
      "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))