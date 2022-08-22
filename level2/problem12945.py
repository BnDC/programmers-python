def solution(n):
    a, b = 0, 1

    for _ in range(n - 1):
        a, b = b, a + b

    return b % 1234567

print(solution(3) == 2)
print(solution(5) == 5)
