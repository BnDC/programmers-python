def solution(n, computers):
    visited    = [False] * n
    network    = n
    visited[0] = True
    
    def dfs(v):
        nonlocal network
        for i, v in enumerate(computers[v]):
            if not visited[i]:
                visited[i] = True
                if v == 1:
                    network -= 1 
                dfs(i)
    
    dfs(0)
    
    return network
    
# print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
# print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
print(solution(4, [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]))