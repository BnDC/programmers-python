def solution(n, lost, reserve):
    answer = 0
    lost.sort()

    for e in reversed(lost):
        if e in reserve:
            lost.remove(e)
            reserve.remove(e)

    for e in reversed(lost):
        if e+1 in reserve:
            lost.remove(e)
            reserve.remove(e+1)

        elif e-1 in reserve:
            lost.remove(e)
            reserve.remove(e-1)

    answer = n - len(lost)

    return answer
