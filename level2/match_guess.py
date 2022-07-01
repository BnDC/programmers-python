def solution(n, a, b):
    answer = 1

    if a > b:
        a, b = b, a

    while not (a % 2 != 0 and b % 2 == 0 and b - a == 1):
        a = a // 2 + 1 if a % 2 != 0 else a // 2
        b = b // 2 + 1 if b % 2 != 0 else b // 2
        answer += 1
        
    return answer