def solution(s, n):
    answer = ''
    n = n % 26
    for i in range(len(s)):
        d = ord(s[i])
        if s[i] == ' ':
            answer += ' '

        else:
            if s[i] == s[i].upper() and d+n >= 90:
                answer += chr(d+n - 26)
            elif s[i] == s[i].lower() and d+n >= 122:
                answer += chr(d+n - 26)
            else:
                answer += chr(d+n)

    return answer


print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))
print(solution("abcdefg", 4))
print(solution("AaZz", 25))
