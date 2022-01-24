from collections import deque
import enum
import heapq 

def solution(priorities, location):
    answer = 0
    queue  = deque([(value, idx) for idx, value in enumerate(priorities)])

    while True:
        x = queue.popleft()

        if x[0] < max(queue)[0]:
            queue.append(x)
        
        else:
            answer += 1
            if x[1] == location:
                return answer
            

print(solution([1, 1, 9, 1, 1, 1], 0))
