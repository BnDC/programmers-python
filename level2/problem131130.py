def solution(cards):
    cnt = 0
    length = len(cards)

    groups = []
    is_opened = [False for _ in range(length)]

    while cnt < length:
        now = -1
        for i in range(length):
            if not is_opened[i]:
                now = i
                break

        group = []
        while True:
            if is_opened[now]:
                break
            else:
                is_opened[now] = True
                group.append(cards[now])
                cnt += 1
            now = cards[now] - 1
        groups.append(group)

    lengths = [len(group) for group in groups]
    lengths.sort()

    return lengths[-1] * lengths[-2] if len(lengths) > 1 else 0


print(solution([8, 6, 3, 7, 2, 5, 1, 4]) == 12)
