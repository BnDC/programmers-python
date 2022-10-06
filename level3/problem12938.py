def solution(n, s):
    if n > s:
        return [-1]
    share, remainder = divmod(s, n)
    answer = [share for _ in range(n)]

    for i in range(1, remainder + 1):
        answer[-i] += 1
    return answer


print(solution(2, 9) == [4, 5])
print(solution(2, 1) == [-1])
print(solution(2, 8) == [4, 4])
