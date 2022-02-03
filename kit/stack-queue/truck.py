import collections

def solution(bridge_length, weight, truck_weights):
    answer = 0
    stack  = []
    queue  = collections.deque()
    arrived_truck = []
    all = len(truck_weights)
    trucks = [[truck, 0] for truck in reversed(truck_weights)]
    next = None

    while len(stack) < all:
        if next:
            stack.append(next)

        #print(trucks)
        #print(queue)

        if trucks and sum(e[0] for e in queue) + trucks[-1][0] <= weight:
            queue.append(trucks.pop())
        
        answer += 1
        for q in queue:
            #print(q)
            q[1] += 1
            
        
        if queue and queue[0][1] == bridge_length:
            next = queue.popleft()
        else:
            next = None
        
    print(answer)

    return answer

# 첫번째 풀이 왜 틀린지 몰라서 백지부터 다시 작성
print(solution(2, 10, [7, 4, 5, 6]))