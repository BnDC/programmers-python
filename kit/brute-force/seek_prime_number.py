from itertools import permutations
from math import sqrt


def is_prime_number(number):

    n = int(sqrt(number)) + 1

    if number == 0 or number == 1:
        return False

    elif number == 2 or number == 3:
        return True

    for i in range(2, n):
        if number % i == 0:
            return False

    return True


def solution(numbers):
    answer = 0
    prime_numbers = list(map(int, numbers))

    for i in range(2, len(prime_numbers)+1):
        prime_numbers += [int(''.join(number))
                          for number in list(permutations(numbers, i))]

    prime_numbers = list(set(prime_numbers))

    for number in prime_numbers:
        if is_prime_number(number):
            answer += 1

    return answer
