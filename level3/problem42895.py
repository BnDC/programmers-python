import sys


def get_connect_num(num, n):
    result = num
    for i in range(n - 1):
        result *= 10
        result += num
    return result


def solution(N, number):
    answer = sys.maxsize
    dp = [set() for _ in range(9)]
    dp[1].add(N)
    if N == number:
        return 1
    
    for i in range(2, 9):
        dp[i].add(get_connect_num(N, i))
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i - j]:
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(a * b)
                    if b != 0:
                        dp[i].add(a // b)
        if number in dp[i]:
            answer = min(answer, i)
    # print(dp)
    return answer if answer != sys.maxsize else -1


print(solution(5, 12) == 4)
print(solution(2, 11) == 3)