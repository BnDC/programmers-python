over_ten = [chr(i) for i in range(ord('A'), ord('F') + 1)]

def convert_n_notation(num, n):
    if num == 0:
        return ['0']

    result = []
    while num != 0:
        s = num % n
        if s >= 10:
            s = over_ten[s % 10]
        s = str(s)
        result.append(s)
        num //= n

    return list(reversed(result))


def solution(n, t, m, p):
    answer = []
    game = []
    start = 0
    while len(answer) != t:
        while len(game) < m:
            game.extend(convert_n_notation(start, n))
            start += 1
        answer.extend(game[p - 1])
        game = game[m:]
    return ''.join(answer)


print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))
