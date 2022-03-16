def solution(jobs):
    # n = len(jobs)
    total = 0
    time = 0
    jobs.sort(key=lambda x: x[1])
    i = 0

    while i < len(jobs):
        if jobs[i][0] <= time and jobs[i][1] != -1:
            total += time - jobs[i][0] + jobs[i][1]
            time += jobs[i][1]
            i += 1

        elif jobs[i][1] == -1:
            i += 1

        else:
            j = i + 1
            ifb = 0
            # while j < len(jobs):
            for j in range(i + 1, len(jobs)):
                if jobs[j][0] <= time:
                    total += time - jobs[j][0] + jobs[j][1]
                    time += jobs[j][1]
                    jobs[j][1] = -1
                    ifb = 1
                    break
            
            # 추가
            if ifb == 0:
                time += 1
            
            continue

    return total // len(jobs)