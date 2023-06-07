import math


def solution(arrayA, arrayB):
    ga = 0
    for i in range(len(arrayA)):
        ga = math.gcd(ga, arrayA[i])

    for b in arrayB:
        if b % ga == 0:
            ga = 0
            break

    gb = 0
    for i in range(len(arrayB)):
        gb = math.gcd(gb, arrayB[i])

    for a in arrayA:
        if a % gb == 0:
            gb = 0
            break
    answer = max(ga, gb)

    return answer if answer > 1 else 0


print(solution([10, 17], [5, 20]) == 0)
print(solution([10, 20], [5, 17]) == 10)
print(solution([14, 35, 119], [18, 30, 102]) == 7)
