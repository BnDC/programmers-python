def solution(distance, rocks, n):
    answer = 0
    total = len(rocks)
    left = 0
    right = distance

    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        base = 0
        for rock in rocks:
            if base + mid <= rock:
                cnt += 1
                base += rock # (2)

        if cnt + n < total:
            # if total - cnt < n:
            right = mid - 1
        else:
            left = mid + 1

    return mid


print(solution(25, [2, 14, 11, 21, 17], 2))