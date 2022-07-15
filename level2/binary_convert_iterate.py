def solution(s):
    zero_counter, convert_counter = 0, 0
    while s != "1":
        zero_counter += s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:]
        convert_counter += 1
    return [convert_counter, zero_counter]

print(solution("110010101001"))