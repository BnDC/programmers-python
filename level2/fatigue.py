import itertools

def solution(k, dungeons):
    n = len(dungeons)
    permu = itertools.permutations(dungeons, n)
    answer = 0
    cnt = 0

    for p in permu:
        fatigue = k
        cnt = 0
        for need, consumed in p:
            if fatigue >= need:
                fatigue -= consumed
                cnt += 1
        answer = max(answer, cnt)

    return answer

print(solution(80, [[80, 20], [50, 40], [30, 10]]))