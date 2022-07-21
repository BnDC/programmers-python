
from re import S


def solution(n, words):
    answer = [0, 0]
    records = set()

    '''
    1 ~ n, 2 ~ 100
    words = [a, b, c], a: 2 ~ 50, a -> "abcdef..."

    탈락자 O
        answer = [탈락자 번호, 차례]
    탈락자 X
        answer = [0, 0]
    '''
    person = 0
    people = [0] * (n + 1)

    for i in range(len(words)):
        person = (person % n) + 1
        people[person] += 1
        if words[i] in records or (i != 0 and words[i - 1][-1] != words[i][0]):
            answer = [person, people[person]]
            break
        else:
            records.add(words[i])

    return answer

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))