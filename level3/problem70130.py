import collections


def solution(a):
    answer = -1
    counter = collections.Counter(a)
    n = len(a)

    items = list(counter.items())
    items.sort(key=lambda x: x[1])

    for num, counted in items:
        if answer >= counted:
            continue
        i, cnt = 0, 0
        while i < n - 1:
            if a[i] != num and a[i + 1] != num \
                    or a[i] == a[i + 1]:
                i += 1
                continue
            i += 2
            cnt += 1
        answer = max(answer, cnt)

    if answer == -1:
        return 0

    return answer * 2
