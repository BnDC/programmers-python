def solution(s):
    stack = []

    for i in s:
        stack.append(i)
        while len(stack) >= 2 and stack[-2] == stack[-1]:
            stack.pop()
            stack.pop()

    return 1 if len(stack) == 0 else 0