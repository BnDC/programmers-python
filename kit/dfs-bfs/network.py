def solution(n, computers):
    visited    = [False] * n
    network    = n
    #visited[0] = True
    
    def dfs(v):
        nonlocal network
        for i, connected in enumerate(computers[v]):
            if not visited[i] and connected == 1:
                visited[i] = True
                # if conected == 1 and before != None:
                if v != i:
                    network -= 1
                dfs(i)
    
    for i in range(len(visited)):
        if not visited[i]:
            dfs(i)
    
    return network
    
# print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
# print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
# print(solution(4, [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]))
# print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]), 2)
# print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]), 1)
print(solution(3, [[1, 0, 1], [0, 1, 0], [1, 0, 1]]), 2)
print(solution(4, [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]]), 1)
# print(solution(4, [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]), 4)