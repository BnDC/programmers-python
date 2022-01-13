from math import ceil


def solution(progresses, speeds):
    COMPLETE = 100
    stack = [ceil((COMPLETE - progresses[idx])/speeds[idx])
             for idx in range(len(progresses)-1, -1, -1)]
    answers = []

    while stack:
        answer = 1
        x = stack.pop()
        while stack and x >= stack[-1]:
            stack.pop()
            answer += 1

        answers.append(answer)

    return answers
