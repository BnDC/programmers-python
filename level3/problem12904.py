def solution(s):
    answer = 0
    n = len(s)
    for start in range(n):
        for length in range(1, n - start + 1):
            now = s[start: start + length]
            if now == now[::-1]:
                answer = max(answer, len(now))
    return answer


print(solution("abcdcba") == 7)
print(solution("abacde") == 3)
