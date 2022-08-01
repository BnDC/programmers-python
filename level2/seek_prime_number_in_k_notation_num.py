from typing import *


def list_to_int(n: List[int]) -> int:
    result = 0
    for i in n:
        result = result * 10 + i
    return result


def is_prime_number(n: List[int]) -> int:
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def convert_n_k_notation(n: int, k: int) -> List[int]:
    result = []
    while n != 0:
        result.append(n % k)
        n //= k
    return list(reversed(result))


def seek_candidates(converted_n: List[int]) -> List[List[int]]:
    zero_list = [i for i in range(len(converted_n)) if converted_n[i] == 0]
    if len(zero_list) == 0:
        return [converted_n]

    candidates = [converted_n[:zero_list[0]]]
    for i in range(len(zero_list) - 1):
        candidate = converted_n[zero_list[i] + 1: zero_list[i + 1]]
        if candidate:
            candidates.append(candidate)

    last = converted_n[zero_list[-1] + 1:]
    if last:
        candidates.append(last)

    return candidates


def solution(n, k):
    answer = 0
    converted_n = convert_n_k_notation(n, k)
    candidates = seek_candidates(converted_n)

    for candidate in candidates:
        if is_prime_number(list_to_int(candidate)):
            answer += 1

    return answer


print(solution(437674, 3))
print(solution(110011, 10))
