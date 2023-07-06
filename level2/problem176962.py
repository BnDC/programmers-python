def solution(plans):
    answer = []
    sorted_plans = []
    length = len(plans)

    for i in range(length):
        name, start, time = plans[i]
        hour, minute = map(int, start.split(":"))
        sorted_plans.append((name, hour * 60 + minute, int(time)))
    sorted_plans.sort(key=lambda x: x[1])

    print(sorted_plans)

    stack = []
    for i in range(length - 1):
        now_name, now_start, now_time = sorted_plans[i]
        next_name, next_start, next_time = sorted_plans[i + 1]

        if now_start + now_time > next_start:
            stack.append((now_name, now_time - (next_start - now_start)))
        else:
            answer.append(now_name)
            now_start += now_time
            if now_start == next_start: continue
            while stack:
                extra_name, extra_time = stack.pop()
                nx = now_start + extra_time
                if nx > next_start:
                    stack.append((extra_name, nx - next_start))
                    break
                answer.append(extra_name)
                now_start = nx
    answer.append(sorted_plans[length - 1])

    while stack:
        name, _ = stack.pop()
        answer.append(name)

    return answer


print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]))
