def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    
    for idx,citation in enumerate(citations):
        if len(citations[:idx + 1]) <= citation:
            answer = idx + 1

    return answer

print(solution([3, 0, 6, 1, 5]))