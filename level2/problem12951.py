def solution(s):
    return ' '.join(e.capitalize() for e in s.split(" "))


print(solution("3people unFollowed me") == "3people Unfollowed Me")
print(solution("for the last week") == "For The Last Week")
