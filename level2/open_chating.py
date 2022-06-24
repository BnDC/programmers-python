def solution(record):
    result = []
    name_dict = dict()
    
    for rec in record:
        tmp = rec.split(" ")
        if tmp[0] == "Leave":
            continue
        name_dict[tmp[1]] = tmp[2]

    for rec in record:
        tmp = rec.split(" ")
        if tmp[0] == "Change":
            continue

        if tmp[0] == "Enter":
            result.append(name_dict[tmp[1]] + "님이 들어왔습니다.")
        else:
            result.append(name_dict[tmp[1]] + "님이 나갔습니다.")
        
    return result