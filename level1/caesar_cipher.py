def solution(s, n):
    answer = ''
    for i in range(len(s)):
        d = ord(s[i])
        if s[i] == ' ':
            answer += ' '
        else:
            if (d <= 90 and d+n > 90) or d+n > 122:
                answer += chr(d+n-26)
            elif 65 <= d+n <= 90 or 97 <= d+n <= 122:
                answer += chr(d+n)
    return answer


print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))
print(solution("abcdefg", 4))
print(solution("AaZz", 25))  # *
# 등호 잘못 처리
