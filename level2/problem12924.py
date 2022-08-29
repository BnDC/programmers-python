import collections


def solution(n):
    result = collections.deque()
    answer = 0
    sum_ = 0

    i = 1
    while i < 10000:
        if sum_ == n:
            answer += 1

        if sum_ < n:
            result.append(i)
            sum_ += i
            i += 1
        else:
            sum_ -= result.popleft()

        if len(result) == 0:
            break
    return answer


print(solution(15) == 4)