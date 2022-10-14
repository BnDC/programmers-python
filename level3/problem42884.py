def solution(routes):
    answer = 0
    now = -30001
    routes.sort(key=lambda x: x[1])

    for start, end in routes:
        if now < start:
            answer += 1
            now = end
    return answer


print(solution([[-20, -15], [-14, 5], [-18, -13], [-5, -3]]) == 2)
