def solution(n, times):
    answer = 0
    times.sort()
    left  = 0
    right = n * times[0]
    
    while left < right:    
        
        mid = (left + right) // 2
        answer = 0
    
        for time in times:
            answer += (mid // time)
            if answer >= n:
                break
        
        if n <= answer:
            right = mid - 1
        elif n > answer:
            left = mid + 1
        
    return left

# print(solution(6, [7, 10]))
print(solution(10, [5, 15]))