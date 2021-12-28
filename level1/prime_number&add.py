def solution(left, right):
    answer = 0

    def seek_factor(number):
        cnt = 0

        for i in range(1, number+1):
            if number % i == 0:
                cnt += 1

        return cnt

    for num in range(left, right + 1):
        if seek_factor(num) % 2 == 0:
            answer += num
        else:
            answer -= num

    return answer


print(solution(13, 17))
