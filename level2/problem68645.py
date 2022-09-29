def solution(n):
    answer = []
    dx = [1, 0, -1]
    dy = [0, 1, -1]

    x, y = 0, 0
    sum_ = n * (n + 1) // 2
    cnt = 1

    tri = [[0] * (i + 1) for i in range(n)]
    tri[x][y] = cnt
    cnt += 1

    i = 0
    while cnt <= sum_:
        while True:
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or n <= nx or ny < 0 or nx + 1 <= ny or tri[nx][ny] != 0:
                break
            tri[nx][ny] = cnt
            x, y = nx, ny
            cnt += 1
        i = (i + 1) % 3

    for l in tri:
        answer.extend(l)
    return answer


print(solution(4) == [1, 2, 9, 3, 10, 8, 4, 5, 6, 7])
print(solution(5) == [1, 2, 12, 3, 13, 11, 4, 14, 15, 10, 5, 6, 7, 8, 9])
print(solution(6) == [1, 2, 15, 3, 16, 14, 4, 17, 21, 13, 5, 18, 19, 20, 12, 6, 7, 8, 9, 10, 11])
