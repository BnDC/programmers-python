def solution(n, l, r):
    answer = 0
    for i in range(l - 1, r):
        if check(i): answer += 1
    return answer


def check(i):
    if i % 5 == 2: return False
    if i < 5: return True
    return check(i // 5)


print(solution(2, 4, 17) == 8)
