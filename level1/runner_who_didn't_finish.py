def solution(participant, completion):

    for person in participant:
        if person not in completion:
            return person

        completion.remove(person)


# print(solution(["mislav", "stanko", "mislav", "ana"],
#       ["stanko", "ana", "mislav"]))
