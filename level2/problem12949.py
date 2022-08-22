def solution(arr1, arr2):
    m = len(arr1)
    s = len(arr1[0])
    n = len(arr2[0])
    answer = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            for k in range(s):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer


print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]) == [[15, 15], [15, 15], [15, 15]])
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]) == [[22, 22, 11], [36, 28, 18],
                                                                                         [29, 20, 14]])
