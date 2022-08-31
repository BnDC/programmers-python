def solution(n):
    answer = ""
    while n != 0:
        if n % 3 != 0:
            answer += str(n % 3)
            n //= 3
        else:
            answer += "4"
            n = n // 3 - 1
    return answer[::-1]


print(solution(1) == "1")
print(solution(2) == "2")
print(solution(3) == "4")
print(solution(4) == "11")
print(solution(5) == "12")

print(solution(6) == "14")
print(solution(7) == "21")
print(solution(8) == "22")
print(solution(9) == "24")
print(solution(10) == "41")
