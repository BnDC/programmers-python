def solution(progresses, speeds):
    COMPLETE = 100
    durations = []
    stack = []
    answers = []

    for idx in range(len(progresses)-1, -1, -1):
        duration = 1
        while speeds[idx]*duration < COMPLETE - progresses[idx]:
            duration += 1
        stack.append(duration)

    while stack:
        answer = 1
        x = stack.pop()
        while stack and x >= stack[-1]:
            stack.pop()
            answer += 1

        answers.append(answer)

    return answers
