def solution(n, times):
    answer = 0
    times.sort()
    left  = 0
    right = n * times[0]
    
    while answer != n:    
        
        mid = (left + right) // 2
        answer = 0
        for time in times:
            answer += (mid // time)
        
        if n < answer:
            right = mid
        elif n > answer:
            left = mid
        else:
            break
    
    mid -= mid % times[0]
        
    return mid
    

# print(solution(6, [7, 10]))
print(solution(10, [5, 15]))