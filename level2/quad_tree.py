def solution(arr):
    result = []

    def dfs(start_x, start_y, length):
        color = arr[start_x][start_y]

        for i in range(length):
            for j in range(length):
                if color != arr[start_x + i][start_y + j]:
                    dfs(start_x, start_y, length // 2)
                    dfs(start_x, start_y + length // 2, length // 2)
                    dfs(start_x + length // 2, start_y, length // 2)
                    dfs(start_x + length // 2, start_y + length // 2, length // 2)
                    return
        result.append(color)
        return

    dfs(0, 0, len(arr))

    return [result.count(0), result.count(1)]


print(solution([
    [1, 1, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
    [1, 1, 1, 1]
]))
