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
            right = mid # 이 부분 바꾸니까 답
        elif n > answer:
            left = mid + 1
    
    # mid -= mid % times[0]
        
    return left