# fourth - try: 3, 12실패

def solution(phone_book):
    phone_book.sort(key=lambda x: len(x))
    hash_map = {}
    before_length = len(phone_book[0])

    for i in range(len(phone_book)):
        current_length = len(phone_book[i])
        hash_map[phone_book[i]] = 1

    if current_length != before_length:
            for sliced_number in [number[:before_length] for number in phone_book[i+1:]]:
                if hash_map.get(sliced_number):  # not 실수 주의
                    # print(sliced_number)
                    return False
        before_length = current_length

    return True


print(solution(["12", "456789", "23", "34", "456"]))  # error
'''
["12", "23", "34", "456", "456789"]
"456"의 경우 
두 글자가 다 검사가 안끝났음에도,
세 글자 검사로 넘어가게 되는 문제 발생
근데 검사를 두 글자로 함
'''
