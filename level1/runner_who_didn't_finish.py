
def solution(participant, completion):

    participant.sort()
    completion.sort()

    print("search_start")
    if participant[-1] != completion[-1]:
        return participant[-1]

    participant.pop()

    while len(participant) != 1:
        cnt = len(participant)

        front_half_participant = participant[:cnt//2]
        back_half_participant = participant[cnt//2:]
        front_half_completion = completion[:cnt//2]
        back_half_completion = completion[cnt//2:]

        if front_half_participant != front_half_completion:
            participant = front_half_participant
            completion = front_half_completion

        elif back_half_participant != back_half_completion:
            participant = back_half_participant
            completion = back_half_completion

    return participant[0]


'''
def solution(participant, completion):
    participant.sort()
    completion.sort()

    start = time.time()
    if participant[-1] != completion[-1]:
        end = time.time()
        print(f"{(end-start):.11f} s")
        return participant[-1]

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            end = time.time()
            print(f"{(end-start):.11f} s")
            return participant[i]
    # return participant[len(participant)-1]
'''

print(solution([
    "a", "b", "c", "d", "e", "f", "g",
    "h", "i", "j", "k", "l", "m", "n",
    "o", "p", "q", "r", "s", "t", "u",
    "v", "w", "x", "y", "z", "l"
],
    [
    "a", "b", "c", "d", "e", "f", "g",
    "h", "i", "j", "k", "l", "m", "n",
    "o", "p", "q", "r", "s", "t", "u",
    "v", "w", "x", "y", "z"
],
))
