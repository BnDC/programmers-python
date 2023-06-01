def solution(book_time):
    answer = 0
    MAX_TIME = 24 * 60
    time = [0 for _ in range(MAX_TIME)]

    for s, e in book_time:
        start, end = parse_time(s), parse_time(e)
        end += 10

        time[start] += 1
        if end < MAX_TIME:
            time[end] -= 1

    for i in range(1, MAX_TIME):
        time[i] += time[i - 1]
        answer = max(answer, time[i])

    return answer


def parse_time(t: str):
    h, m = t.split(":")
    return int(h) * 60 + int(m)
