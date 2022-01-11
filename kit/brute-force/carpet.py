def seek_divisor(number):
    if number == 1:
        return {1}

    divisors = set()
    divisor = 1
    i = 2

    if (number ** 0.5).is_integer():
        divisors.add(int(number ** 0.5))

    while number != 1:
        if number % i == 0:
            divisor *= i
            divisors.add(divisor)
            divisors.add(number//i)
            number //= i
            i = 1
        i += 1

    return sorted(list(divisors))


def solution(brown, yellow):
    answer = []
    area = brown + yellow
    yellow_divisors = seek_divisor(yellow)
    print(yellow_divisors)

    for divisor in yellow_divisors:
        divisor_pair = yellow//divisor

        border = 2*(divisor+divisor_pair)+4

        if border == brown:
            answer = [divisor+2, divisor_pair+2]

    answer.sort(reverse=True)

    return answer
