def solution(n, info):
    max_diff = 0

    answer = [-1]
    lion = [0 for _ in range(11)]

    def dfs(depth, remain, arr):
        nonlocal max_diff, answer
        if remain == 0:
            score = get_score(info, arr)
            if max_diff < score:
                max_diff = score
                answer = arr[:]
            elif score != 0 and max_diff == score:
                for i in range(10, -1, -1):
                    if answer[i] < arr[i]:
                        answer = arr[:]
                        break
                    elif answer[i] > arr[i]:
                        break
            return

        for i in range(depth, 11):
            arr[i] += 1
            dfs(i, remain - 1, arr)
            arr[i] -= 1
        return

    dfs(0, n, lion)
    return answer


def get_score(arr1, arr2):
    global max_score
    score1, score2 = 0, 0
    for i in range(11):
        if arr1[i] == 0 and arr2[i] == 0:
            continue

        if arr1[i] >= arr2[i]:
            score1 += 10 - i
        else:
            score2 += 10 - i
    return score2 - score1 if score2 > score1 else 0


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]) == [0, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0])
print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [-1])
print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]) == [1, 1, 2, 0, 1, 2, 2, 0, 0, 0, 0])
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]) == [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2])
