from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue:
        item = queue.popleft()
        cnt = 0

        for e in queue:
            cnt += 1
            if e < item:
                break

        answer.append(cnt)

    return answer

print(solution([1, 2, 3, 2, 3]))