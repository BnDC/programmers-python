def get_gcd(a, b):
    if a % b == 0: return b
    return get_gcd(b, a % b)


def get_lcm(a, b):
    return a * b // get_gcd(a, b)


def solution(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    arr.sort()
    answer = arr[0]

    for i in range(1, n):
        answer = get_lcm(answer, arr[i])
    return answer


print(solution([2, 6, 8, 14]) == 168)
print(solution([2, 6, 8, 14]) == 168)
