def solution(msg):
    answer = []
    dictionary = {chr(i): i - 64 for i in range(65, 65 + 26)}
    dictionary_cnt = 27

    while msg != "":
        for length in range(len(msg), -1, -1):
            matching_word = dictionary.get(msg[:length])
            if matching_word is not None:
                answer.append(matching_word)
                dictionary[msg[:length + 1]] = dictionary_cnt

                msg = msg[length:]
                dictionary_cnt += 1
                break

    return answer


print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
