def solution(s):
    s_list = list(map(int, s.split(" ")))
    s_list.sort()
    return str(s_list[0]) + " " + str(s_list[-1])


print(solution("1 2 3 4") == "1 4")
print(solution("-1 -2 -3 -4") == "-4 -1")
print(solution("-1 -1") == "-1 -1")
