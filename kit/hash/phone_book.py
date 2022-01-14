# third - try: 실패
import collections


def solution(phone_book):
    phone_book.sort(key=lambda x: len(x))
    hash_map = collections.defaultdict(int)
    m = -1

    for i in range(len(phone_book)):
        n = len(phone_book[i])
        if n == m:
            continue

        elif n == len(phone_book[-1]):
            return True

        for sliced_number in [number[:n] for number in phone_book]:
            if hash_map[sliced_number] == 0:
                hash_map[sliced_number] += 1
                # print(hash_map)
            else:
                return False
        m = n

    return True

#print(solution(["119", "97674223", "1195524421"]))
# print(solution(["123","456","789"]))
# print(solution(["12","123","1235","567","88"]))


'''
그 자체로 접두사가 아닌 원소에 포함된 문자가 딕셔너리에 저장해
ex ["1234", "1235"]

실패
'''
