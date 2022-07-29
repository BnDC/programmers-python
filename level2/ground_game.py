def seek_max(row, column, land):
    columns = [0, 0, 0, 0]
    columns[column] = 1
    result = land[row][column]

    for i in range(4):
        if columns[i] == 0:
            result = max(result, land[row][column] + land[row - 1][i])
    return result


def solution(land):
    row = len(land)
    for i in range(1, row):
        for j in range(0, 4):
            land[i][j] = seek_max(i, j, land)
    return max(land[row - 1])


print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
