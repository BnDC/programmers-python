def solution(number, k):
    answer = ''
    n      = len(number)
    start  = 0
    end = start + k + 1

    digit_number = n - k

    while True:
        max_number = '-' # max_number가 '0'으로 초기화시 number에 0이 포함되어있을 때 문제 발생
        max_idx = 0
        for i in range(start, end):
            if max_number < number[i]:
                max_number = number[i]
                max_idx = i

            if max_number == '9':  # 추가 -> 8번 실패
                break  # 추가 -> 8번 실패

        answer += number[max_idx]

        k -= max_idx - start
        digit_number -= 1
        start = max_idx + 1
        end = min(start + k + 1, n)

        if k <= 0:
            answer += number[start:]
            break

        if digit_number == 0:
            break

    return answer


# print(solution("1924", 2))
# print(solution("1231234", 3))
# print(solution("4177252841", 4))

number = '935921'
k      = 5

print('before_n: ', len(number))
print()


result = solution(number, k)
print('after_n: ', len(number))
print(result)