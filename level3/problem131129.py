import collections


def solution(target):
    _MAX = 1000000
    dp = [[_MAX, _MAX] for i in range(target + 1)]

    q = collections.deque()
    q.append((0, 0, 0))

    while q:
        now, cnt, weight = q.popleft()

        for i in range(1, 20 + 1):
            for j in range(1, 3 + 1):
                _next = i * j + now
                if _next > target:
                    continue
                next_weight = weight + 1 if j == 1 else weight
                if dp[_next][0] > cnt + 1 or (dp[_next][0] == cnt + 1 and dp[_next][1] < next_weight):
                    dp[_next] = [cnt + 1, next_weight]
                    q.append((_next, cnt + 1, next_weight))

        _next = now + 50
        next_weight = weight + 1
        if _next > target:
            continue

        if dp[_next][0] > cnt + 1 or (dp[_next][0] == cnt + 1 and dp[_next][1] < next_weight):
            dp[_next] = [cnt + 1, next_weight]
            q.append((_next, cnt + 1, next_weight))

    return dp[-1]


print(solution(21) == [1, 0])
print(solution(58) == [2, 2])
