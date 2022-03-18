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
    cnt = 0
    h = {}

    queue.append((begin, 0))

    while queue:
        now, cnt = queue.popleft()
        cnt += 1
        for word in words:
            # if len(set(word) - set(now)) == 1 or len(set(now) - set(word)) == 1:
            if compare(now, word) == 1:
                queue.append((word, cnt))
                if word not in h:
                    h[word] = cnt
                else:
                    h[word] = min(h[word], cnt)
        if now in words:
            words.remove(now)

    return h[target]


# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
# print(solution("hit", "cog", ["cog", "log", "lot", "dog", "dot", "hot"]))
# print(solution("aoa", "aof", ["aob", "aoc", "aod", "aof", "aoe"]))
# print(solution("aaa", "aab", ["aab"]))
# print(solution("hit", "hhh", ["hhh", "hht"]))
print(solution('aaa', 'abc', ['aaz', 'aab', 'abb', 'abc']))