LAST_SECOND = 360001


def str2int(time):
    hour, minute, second = time.split(":")
    return 3600 * int(hour) + 60 * int(minute) + int(second)


def int2str(second):
    hour, remain = divmod(second, 3600)
    minute, second = divmod(remain, 60)
    return '{0:02d}:{1:02d}:{2:02d}'.format(hour, minute, second)


def solution(play_time, adv_time, logs):
    dp = [0 for _ in range(LAST_SECOND)]

    for log in logs:
        time = log.split("-")
        start, end = str2int(time[0]), str2int(time[1])
        dp[start] += 1
        dp[end] -= 1

    for i in range(1, LAST_SECOND):
        dp[i] += dp[i - 1]

    term = str2int(adv_time)
    window = sum(dp[:term])
    max_window = window
    max_idx = 0

    for i in range(1, LAST_SECOND - term):
        window = window - dp[i - 1] + dp[i + term - 1]
        if max_window < window:
            max_window = window
            max_idx = i
    return int2str(max_idx)


print(solution("02:03:55", "00:14:15",
               ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29",
                "01:37:44-02:02:30"]) == "01:30:59")

print(solution("99:59:59", "25:00:00",
               ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]) == "01:00:00")

print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]) == "00:00:00")
