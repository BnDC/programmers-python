# second try : 11, 14 실패
import collections


def solution(phone_book):
    phone_book.sort(key=lambda x: len(x))
    hash_map = collections.defaultdict(int)

    n = len(phone_book[0])

    for number in phone_book:
        for idx in range(n, len(number)+1):
            if hash_map[number[:idx]] == 0:
                hash_map[number[:idx]] += 1
                # print(hash_map)
            else:
                return False

    return True

#print(solution(["119", "97674223", "1195524421"]))
# print(solution(["123","456","789"]))
# print(solution(["12","123","1235","567","88"]))
