def solution(brown, yellow):
    answer = []

    for divisor in range(1, yellow+1):
        if yellow % divisor != 0:
            continue

        divisor_pair = yellow//divisor

        border = 2*(divisor+divisor_pair) + 4

        if border == brown:
            answer = [divisor+2, divisor_pair+2]

    answer.sort(reverse=True)

    return answer
