def seek_max_divisor(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            result = max(i, n // i)
            if result <= int(1e7):
                return result
    return -1


def solution(begin, end):
    answer = []

    for i in range(begin, end + 1):
        max_divisor = seek_max_divisor(i)

        if max_divisor != -1:
            answer.append(max_divisor)
        else:
            if i == 1:
                answer.append(0)
            else:
                answer.append(1)
    return answer


print(solution(1, 10))
