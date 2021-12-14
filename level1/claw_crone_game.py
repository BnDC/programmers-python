def solution(board, moves):
    answer = 0
    basket = []

    for move in moves:
        for i in range(len(board)):
            if board[i][move-1]:
                if basket and basket[-1] == board[i][move-1]:
                    basket.pop()
                    answer += 1
                    board[i][move-1] = 0
                    break

                else:
                    basket.append(board[i][move-1])
                    board[i][move-1] = 0
                    break

    return answer


board = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 3],
    [0, 2, 5, 0, 1],
    [4, 2, 4, 4, 2],
    [3, 5, 1, 3, 1],
]

moves = [1, 5, 3, 5, 1, 2, 1, 4]

#basket = [4, 3, 1, 1, 3, 2, 2, 4]

print(solution(board, moves))
