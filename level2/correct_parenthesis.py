def solution(s):
    stack = []

    for l in s:
        if l == ")" and stack and stack[-1] == "(":
            stack.pop()
        elif l == "(":
            stack.append(l)
        else:
            return False
    return len(stack) == 0


print(solution("()()"))
print(solution("(())()"))

print(solution(")()("))
print(solution("(()("))
