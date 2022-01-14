# first - try
def solution(phone_book):
    phone_book.sort(key=lambda x: len(x))
    hash_map = []

    for i in range(len(phone_book) - 1):
        n = len(phone_book[i])
        if i == 0 or len(phone_book[i]) != phone_book[i+1]:
            hash_map = list(map(hash, [number[:n]
                            for number in phone_book[i+1:]]))

        else:
            hash_map = hash_map[1:]

        if hash(phone_book[i]) in hash_map:
            return False

        elif phone_book[i]:
            pass
    return True

#print(solution(["119", "97674223", "1195524421"]))
# print(solution(["123","456","789"]))
# print(solution(["12","123","1235","567","88"]))
