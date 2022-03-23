def solution(n, edge):
    answer = 0
    result = 0
    visited = [False] * (n + 1)
    graph = [[] for i in range(n + 1)]
    
    for v, u in edge:
        if v < u:
            graph[v].append(u)
        else:
            graph[u].append(v)
    
    def dfs(v, cnt):
        nonlocal result
        nonlocal answer
        
        if visited[v]:
            return
        
        visited[v] = True
        cnt += 1

        if result < cnt:
            result = cnt
        elif result == cnt:
            answer += 1
        
        for x in graph[v]:
            dfs(x, cnt)
            
    dfs(1, 0)
        
    return answer + 1
    
print(solution(6, [
    [3, 6], [4, 3], [3, 2], 
    [1, 3], [1, 2], [2, 4], 
    [5, 2]
]))