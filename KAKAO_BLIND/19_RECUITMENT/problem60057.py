def solution(s):
    answer = s
    n = len(s)

    for length in range(1, n // 2 + 1):
        start = s[:length]
        result = ""
        cnt = 0
        for i in range(0, n, length):
            cur = s[i: i + length]
            if start == cur:
                cnt += 1
            else:
                if cnt == 1:
                    result += start
                else:
                    result += str(cnt) + start
                cnt = 1
                start = cur
        if start == cur:
            if cnt != 1:
                result += str(cnt) + cur
            else:
                result += cur

        if len(result) < len(answer):
            answer = result
    return len(answer)

print(solution("aabbaccc") == 7)
print(solution("ababcdcdababcdcd") == 9)
print(solution("abcabcdede") == 8)
print(solution("abcabcabcabcdededededede") == 14)
print(solution("xababcdcdababcdcd") == 17)
