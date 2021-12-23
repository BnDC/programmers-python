def solution(n, lost, reserve):
    answer = 0

    for e in reversed(lost):
        if e in reserve:
            lost.pop()
            reserve.remove(e)

        elif e + 1 in reserve:
            lost.pop()
            reserve.remove(e+1)

        elif e - 1 in reserve:
            lost.pop()
            reserve.remove(e-1)

    answer = n - len(lost)

    return answer
