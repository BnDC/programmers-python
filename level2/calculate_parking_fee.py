import math
import heapq
import collections


def compute_time(t1: str, t2: str):
    out_hour, out_minute = map(int, t2.split(":"))
    in_hour, in_minute = map(int, t1.split(":"))
    return (out_hour - in_hour) * 60 + (out_minute - in_minute)


def calculate_fee(fees, minutes):
    base_minute, base_fee, unit_minute, unit_fee = fees
    if minutes <= base_minute:
        return base_fee
    return base_fee + math.ceil((minutes - base_minute) / unit_minute) * unit_fee


def solution(fees, records):
    answer = []
    records_map = collections.defaultdict(list)
    time_map = collections.defaultdict(int)

    for record in records:
        time, car_number, in_or_out = record.split(" ")
        if in_or_out == "IN":
            records_map[car_number].append(time)
        else:
            in_time = records_map[car_number].pop()
            time_map[car_number] += compute_time(in_time, time)

    for remain_car in records_map.keys():
        if records_map[remain_car]:
            time_map[remain_car] += compute_time(records_map[remain_car].pop(), "23:59")

    heap = []
    for number, time in time_map.items():
        heapq.heappush(heap, (number, calculate_fee(fees, time)))

    while heap:
        cur, time = heapq.heappop(heap)
        answer.append(time)

    return answer


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
           "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(fees, records))
