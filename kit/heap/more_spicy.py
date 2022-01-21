import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)

    if scoville[0] >= K:
    	return 0
    
    while len(scoville) >= 2:
        answer += 1
        
        first  = heapq.heappop(scoville) 
        second = heapq.heappop(scoville)
        new    = first + second*2
        
        heapq.heappush(scoville, new)
        
        if scoville[0] >= K:
            return answer
    
    answer = - 1
    
    return answer

s = [1, 2, 3, 9, 10, 12]
x = [1]
y = [1, 2]

print(solution(s, 7))
print(solution(x, 1))
print(solution(y, 2))
