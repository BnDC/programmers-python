def solution(n, lost, reserve):
    answer = 0

    for e in reversed(lost):
        if e in reserve:
            lost.pop()  # 틀린 부분
            reserve.remove(e)

        elif e + 1 in reserve:
            lost.pop()  # 틀린 부분
            reserve.remove(e+1)

        elif e - 1 in reserve:
            lost.pop()  # 틀린 부분
            reserve.remove(e-1)

    answer = n - len(lost)

    return answer


# 틀린 이유
'''
lost = [1, 2, 3, 4, 5]
reserve = [3, 5]

for 에서 e가 3일때,
의도한 동작은 3이 제거 되는 것이 지만
4가 제거 된다.
(속도 측면에서 remove 안쓰고 pop을 썼지만, 잘못된 선택)

result: [1, 2, 3]

'''
