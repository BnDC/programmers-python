def solution(d, budget):
    answer = 0
    sigma = 0
    cnt = 0
    d.sort()

    for e in d:
        sigma += e
        cnt += 1
        if sigma > budget:
            cnt -= 1
            sigma -= e
            break

    return cnt


print(solution([1, 3, 2, 5, 4], 9))
