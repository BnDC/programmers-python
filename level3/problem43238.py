def solution(n, times):
    times.sort()
    left, right = 0, n * times[0]

    while left < right:
        mid = (left + right) // 2
        answer = 0
        for time in times:
            answer += (mid // time)
            if answer >= n:
                break
        if n <= answer:
            right = mid
        elif n > answer:
            left = mid + 1
    return left


print(solution(6, [7, 10]) == 28)