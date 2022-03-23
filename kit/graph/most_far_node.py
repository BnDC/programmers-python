def solution(n, edge):
    answer  = []
    visited = [False] * (n + 1)
    graph   = [[] for i in range(n + 1)]
    
    for v, u in edge:
        if v < u:
            graph[v].append((u))
        else:
            graph[u].append((v))
    
    def dfs(v, cnt):        
        if visited[v]:
            return
        
        visited[v] = True
        cnt += 1
        
        if len(graph[v]) == 0:
            answer.append(v)
            

        # if result < cnt:
        #     result = cnt
        # elif result == cnt:
        #     answer += 1
        
        for x in graph[v]:
            dfs(x, cnt)

    dfs(1, 0)
        
    return len(answer)