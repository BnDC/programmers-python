def solution(rows, columns, queries):
    answer = []
    matrix = [[0] * (columns + 1) for _ in range(rows + 1)]
    
    # generate matrix
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            matrix[i][j] = (i - 1)*columns + j

    def rotate(x1: int, y1: int, x2: int, y2: int):
        cors = [matrix[x1 + 1][y1]]

        # copy
        for c in range(y1, y2):
            cors.append(matrix[x1][c])
        for r in range(x1, x2):
            cors.append(matrix[r][y2])
        for c in range(y2, y1, -1):
            cors.append(matrix[x2][c])
        for r in range(x2, x1 - 1, -1):
            cors.append(matrix[r][y1])

        cnt = 0

        for i in range(1, rows):
            print(*matrix[i])

        # write
        for c in range(y1, y2):
            matrix[x1][c] = cors[cnt]
            cnt += 1
        for r in range(x1, x2):
            matrix[r][y2] = cors[cnt]
            cnt += 1
        for c in range(y2, y1, -1):
            matrix[x2][c] = cors[cnt]
            cnt += 1
        for r in range(x2, x1, -1):
            matrix[r][y1] = cors[cnt]
            cnt += 1

        for i in range(1, rows):
            print(*matrix[i])

        answer.append(min(cors))
        return

    for x1, y1, x2, y2 in queries:
        rotate(x1, y1, x2, y2)

    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))