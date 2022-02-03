from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    weight_checker = 0
    queue = deque()
    truck_weights_reversed = [[truck_weights[i], 0] for i in range(len(truck_weights) - 1, -1, -1)] 

    while queue or truck_weights_reversed: 
        #while len(queue) <= bridge_length and sum(queue) <= weight: 
        
        if truck_weights_reversed and len(queue) + 1 <= bridge_length and weight_checker + truck_weights_reversed[0][0] <= weight:
            queue.append(truck_weights_reversed.pop())
            weight_checker += queue[-1][0]
        
        answer += 1
        for i in range(len(queue)):
            queue[i][1] += 1
        
        if queue and queue[0][1] == bridge_length:
            weight_checker -= queue.popleft()[0]

    return answer