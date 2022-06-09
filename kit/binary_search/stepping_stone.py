def solution(distance, rocks, n):
    answer = 0
    total = len(rocks)
    left = 0
    right = distance
    
    rocks.sort()

    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        base = 0
        for rock in rocks:
            if base + mid <= rock:
                cnt += 1
                base = rock

        if total - cnt > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1

    return answer