import copy

def solution(name):
    answer  = [0, 0]
    left    = 0
    right   = 0
    # initial_codes = [[65] * len(name)] * 2
    initial_codes = [[65] * len(name) for _ in range(2)]
    name_codes    = [ord(alp) for alp in name]
    alphabet = [i for i in range(65, 91)]
    def count_up_or_down(x):
        cnt = 0
        for i in range(27):
            if x == alphabet[i]:
                cnt = i
                break

            if x == alphabet[25 - i]:
                cnt = i + 1
                break

        return cnt

    while (initial_codes[0] != name_codes) and (initial_codes[1] != name_codes):
        answer[0] += count_up_or_down(name_codes[left])
        answer[1] += count_up_or_down(name_codes[right])

        initial_codes[0][left]  = name_codes[left]
        initial_codes[1][right] = name_codes[right]

        if (left > -len(name_codes) + 1) and initial_codes[0] == name_codes:
            return answer[0]
        elif right < len(name_codes) - 1 and initial_codes[1] == name_codes:
            return answer[1]
        elif right == len(name_codes) - 1 and initial_codes[1] == name_codes:
            return min(answer)

        left  -= 1
        right += 1
        
        answer[0] += 1
        answer[1] += 1

    return min(answer)

# print(solution('JAZ'))
# print(solution('JEROEN'))
# print(solution('JAN'))

print(solution('AAA'))
# print(solution('ZAZAZ'))

# 오답 - !!패착!!
# 정한 방향으로 이동하는 상황만 상정
