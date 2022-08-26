def vaild(queens):
    tx, ty = queens[-1]
    for i in range(len(queens) - 1):
        # 대각선 검사
        if abs(queens[i][0] - tx) == abs(queens[i][1] - ty):
            return False
    return True


def solution(n):
    answer = 0
    queens = []
    col_set = set()

    def dfs(row):
        nonlocal answer
        if len(queens) == n:
            answer += 1
            return

        for col in range(1, n + 1):
            # 열 검사
            if col in col_set:
                continue
            queens.append((row, col))
            col_set.add(col)
            if vaild(queens):
                dfs(row + 1)
            queens.pop()
            col_set.remove(col)
        return

    dfs(1)
    return answer


print(solution(4) == 2)
