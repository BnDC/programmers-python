import collections


def solution(begin, target, words):
    if target not in words:
        return 0

    queue = collections.deque()
    cnt = 0
    h = {}

    queue.append((begin, 0))

    while queue:
        now, cnt = queue.popleft()
        cnt += 1
        for word in words:
            if len(set(word) - set(now)) == 1 or len(set(now) - set(word)) == 1: # 문제
                queue.append((word, cnt))
                if word not in h:
                    h[word] = cnt
                else:
                    h[word] = min(h[word], cnt)
        if now in words:
            words.remove(now)

    return h[target]