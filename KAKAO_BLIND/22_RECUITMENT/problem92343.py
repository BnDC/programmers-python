def solution(info, edges):
    answer = 0
    visited = [0] * (1 << 17)
    left = [-1 for _ in range(17)]
    right = [-1 for _ in range(17)]

    for a, b in edges:
        if left[a] == -1:
            left[a] = b
        else:
            right[a] = b

    def dfs(state, sheep, wolf):
        nonlocal answer
        if visited[state]:
            return
        visited[state] = 1

        if sheep <= wolf:
            return
        if sheep > answer:
            answer = sheep

        for i in range(17):
            if not state & (1 << i):
                continue
            if left[i] != -1:
                dfs(state | 1 << left[i], sheep + (info[left[i]] ^ 1), wolf + info[left[i]])
            if right[i] != -1:
                dfs(state | 1 << right[i], sheep + (info[right[i]] ^ 1), wolf + info[right[i]])
        return

    dfs(1, 1, 0)
    return answer


print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
               [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]) == 5)
print(solution(
    [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
    [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]) == 5)
