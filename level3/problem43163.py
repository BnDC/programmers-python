import collections


def solution(begin, target, words):
    if target not in words:
        return 0

    def compare(first, second):
        cnt = 0
        for i, j in zip(first, second):
            if i != j:
                cnt += 1
        return cnt

    queue = collections.deque()
    h = {}
    queue.append((begin, 0))

    while queue:
        now, cnt = queue.popleft()
        cnt += 1
        for word in words:
            if compare(now, word) == 1:
                queue.append((word, cnt))
                if word not in h:
                    h[word] = cnt
                else:
                    h[word] = min(h[word], cnt)
        if now in words:
            words.remove(now)

    return h[target]


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 4)
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0)
