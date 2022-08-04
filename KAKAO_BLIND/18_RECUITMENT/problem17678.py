import heapq


# 시간 계산 하는 함수 (time: 시각, minute: 더하거나 빼고자 하는 시간)
def calculate_time(time: list, minute: int) -> list:
    cur_hour, cur_minute = time
    cur_minute += minute
    if cur_minute >= 60:
        cur_hour += cur_minute // 60
        cur_minute %= 60
    elif cur_minute < 0:
        cur_hour -= 1
        cur_minute += 60
    return [cur_hour, cur_minute]


# 두 t1, t2를 비교하는 함수 시각 t1이 크면 True, t2가 크면 False
def compare_time(t1: list, t2: list) -> bool:
    h1, m1 = t1
    h2, m2 = t2
    if h1 < h2 or (h1 == h2 and m1 < m2):
        return True
    return False


def solution(n, t, m, timetable):
    heap = []
    time = [9, 0]
    # 최소힙에 크루 들이 온 시각[시, 분]을 넣는다
    for come_time in timetable:
        hour, minute = come_time.split(":")
        heapq.heappush(heap, (int(hour), int(minute)))

    shuttle_cnt = 1
    # 셔틀 버스 운행
    while True:
        shuttle = []
        # 탐승 인원 m명을 뽑아 본다
        for _ in range(m):
            come_time = heapq.heappop(heap)
            # 도착한 시각이 버스가 온 시각 보다 늦으면
            # 그 사람 이후의 사람들은 이 버스에 탑승 하지 못했다
            if compare_time(time, come_time):
                heapq.heappush(heap, come_time)
                break
            shuttle.append(come_time)
            # 모두 출근 했으면 운행 종료
            if not heap:
                break
        # 모두 출근 했거나, 셔틀 운행 횟수가 찼으면 운행 종료
        if not heap or shuttle_cnt >= n:
            break
        time = calculate_time(time, t)
        shuttle_cnt += 1

    # 가장 마지막 셔틀이 비었으면 콘은 그 버스에 탑승
    if not shuttle:
        answer = time
    # 가장 마지막 버스에 자리가 있으면 콘은 그 버스에 탑승
    elif len(shuttle) < m:
        answer = time if compare_time([shuttle[-1][0], shuttle[-1][1]], time) else [shuttle[-1][0], shuttle[-1][1]]
    # 가장 마지막 버스에 자리가 없으면 마지막 사람 보다 1분 일찍 와야 한다.
    else:
        answer = calculate_time([shuttle[-1][0], shuttle[-1][1]], -1)

    return ":".join("{0:02d}".format(i) for i in answer)


if __name__ == "__main__":
    a = 1
    print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
    print(solution(1, 10, 2, ["09:10", "09:09", "08:00"]))
    print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
    print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
    print(solution(1, 1, 1, ["23:59"]))
    print(solution(10, 60, 45,
                   ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
                    "23:59", "23:59", "23:59", "23:59", "23:59"]))
