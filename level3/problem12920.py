def solution(n, cores):
    number = len(cores)
    if n <= number:
        return n
    n -= number
    left, right = 1, max(cores) * n

    while left <= right:
        mid = (left + right) // 2
        result = 0
        for i in range(number):
            result += mid // cores[i]

        if n <= result:
            right = mid - 1
        else:
            left = mid + 1

    for i in range(number):
        n -= right // cores[i]
    right += 1

    for i in range(number):
        if n == 0:
            return i

        if right % cores[i] == 0:
            n -= 1


print(solution(6, [1, 2, 3]))
