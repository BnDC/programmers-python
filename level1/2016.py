def solution(a, b):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    day_of_week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']

    for day in days[:a - 1]:
        total += day

    total += b - 1

    return day_of_week[total % 7]


print(solution(5, 24))
