def solution(number, k):
    answer = ''
    # number = list(map(int, list(number)))
    # number = [int(n) for n in number]
    number = list(number)
    digit_number = len(number) - k

    while k != 0:
        max_num = max(number[:-digit_number + 1])
        answer += max_num
        before_max = number.index(max_num)
        number = number[before_max + 1:]
        k -= before_max
        digit_number -= 1

        if digit_number == len(number):
            answer += ''.join(number)
            break

        if len(number) == 2:
            if k == 1:
                #answer += max(number)
                answer += max(number)
                break

    return answer


print(solution("1924", 2))
# print(solution("1231234", 3))
# print(solution("4177252841", 4))