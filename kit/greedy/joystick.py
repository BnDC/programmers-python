from operator import le


def solution(name):
    answer = 0
    idx    = 0
    difference_list = [ord(alp) - ord('A') if ord(alp) < 78 else ord('Z') - ord(alp) + 1 for alp in name]

    while True:#difference_list != [0]*len(name):
        left, right = 1, 1 
        answer     += difference_list[idx]
        difference_list[idx] = 0 

        while idx-left > -len(name) and difference_list[idx-left] == 0:
            left += 1
        
        while idx+right <len(name) and difference_list[idx+right] == 0:
            right += 1

        idx = idx + 1 if right <= left else idx - 1 
        
        if difference_list == [0]*len(name):
            break
        
        answer += 1

    return answer

# print(solution("JAN"))
# print(solution("JEROEN"))
# print(solution("ABABABAA"))
# print(solution("AABAAAAABBB"))
# print(solution("ABAAAAAAAAABB"))
print(solution("BBBBAAAAAB"))
print(solution("BBBBAAAABA"))
