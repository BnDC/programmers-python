def solution(n, computers):
    visited    = [False] * n
    network    = n
    visited[0] = True
    
    def dfs(v):
        nonlocal network
        for i, v in enumerate(computers[v]):
            if not visited[i] and v == 1:
                visited[i] = True
                network -= 1
                dfs(i)
    
    dfs(0)
    
    return network