def solution(n):
    answer = 0
    n_ternary = ''

    while n != 0:
        n_ternary += str(n % 3)
        n = n // 3

    for i, e in enumerate(n_ternary[::-1]):
        answer += int(e)*(3**i)

    return answer


print(solution(45))
