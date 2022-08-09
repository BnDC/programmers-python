def can_fill(x, y, board):
    for i in range(x):
        if board[i][y] != 0:
            return False
    return True


def find(x, y, height, width, board):
    blank = 0
    last_value = -1
    for i in range(x, x + height):
        for j in range(y, y + width):
            if board[i][j] == 0:
                if not can_fill(i, j, board):
                    return False
                blank += 1
                if blank > 2:
                    return False
            else:
                if last_value == -1:
                    last_value = board[i][j]
                elif last_value != board[i][j]:
                    return False

    for i in range(x, x + height):
        for j in range(y, y + width):
            board[i][j] = 0
    return True


def solution(board):
    n = len(board)
    answer = 0

    while True:
        cnt = 0
        for i in range(n):
            for j in range(n):
                if i < n - 1 and j < n - 2 and find(i, j, 2, 3, board):
                    cnt += 1
                if i < n - 2 and j < n - 1 and find(i, j, 3, 2, board):
                    cnt += 1
        if cnt == 0:
            break
        answer += cnt

    return answer


board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [0, 0, 0, 0, 0, 4, 4, 0, 0, 0],
         [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5],
         [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]

print(solution(board) == 2)
