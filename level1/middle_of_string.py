def solution(s):
    half = (len(s)-1)//2
    return s[half] if len(s) % 2 == 1 else s[half] + s[half+1]
