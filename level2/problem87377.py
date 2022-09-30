import sys


def solution(line):
    n = len(line)
    INF = sys.maxsize

    point = set()

    min_x, max_x = INF, -INF
    min_y, max_y = INF, -INF
    for i in range(n):
        for j in range(i + 1, n):
            dot = get_meet(line[i], line[j])
            if dot is not None:
                if dot[0].is_integer() and dot[1].is_integer():
                    dot[0], dot[1] = int(dot[0]), int(dot[1])
                    min_x, min_y = min(min_x, dot[0]), min(min_y, dot[1])
                    max_x, max_y = max(max_x, dot[0]), max(max_y, dot[1])
                    point.add((dot[0], dot[1]))

    answer = [["."] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]
    for x, y in point:
        answer[max_y - y][x - min_x] = "*"
    return ["".join(answer[i]) for i in range(len(answer))]


def get_meet(l1, l2):
    A, B, E = l1
    C, D, F = l2
    if A * D - B * C == 0:
        return None
    return [(B * F - E * D) / (A * D - B * C), (E * C - A * F) / (A * D - B * C)]


print(
    solution([
        [2, -1, 4],
        [-2, -1, 4],
        [0, -1, 1],
        [5, -8, -12],
        [5, 8, 12]
    ]) == ["....*....",
           ".........",
           ".........",
           "*.......*",
           ".........",
           ".........",
           ".........",
           ".........",
           "*.......*"
           ])

print(solution([
    [0, 1, -1],
    [1, 0, -1],
    [1, 0, 1]]
) == ["*.*"])
print(solution([
    [1, -1, 0],
    [2, -1, 0]
]) == ["*"])
print(solution([
    [1, -1, 0],
    [2, -1, 0],
    [4, -1, 0]
]) == ["*"])
