def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 == 0:
            result = num + 1
        else:
            power = find_zero(num)
            result = num + 2 ** power - 2 ** (power - 1)
        answer.append(result)
    return answer


def find_zero(n):
    cnt = 0
    while n % 2 != 0:
        cnt += 1
        n //= 2
    return cnt


print(solution([2, 7]))
