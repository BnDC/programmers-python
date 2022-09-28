def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    sign = [0, -1, 1]

    c_board = [[0] * (m + 1) for _ in range(n + 1)]

    for type_, r1, c1, r2, c2, degree in skill:
        c_board[r1][c1] += sign[type_] * degree
        c_board[r1][c2 + 1] -= sign[type_] * degree
        c_board[r2 + 1][c1] -= sign[type_] * degree
        c_board[r2 + 1][c2 + 1] += sign[type_] * degree

    for i in range(n):
        for j in range(1, m):
            c_board[i][j] += c_board[i][j - 1]

    for i in range(m):
        for j in range(1, n):
            c_board[j][i] += c_board[j - 1][i]

    for i in range(n):
        for j in range(m):
            board[i][j] += c_board[i][j]

            if board[i][j] >= 1:
                answer += 1
    return answer


print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
               [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]) == 10)

print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]) == 6)
