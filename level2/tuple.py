import collections

def solution(s):
    s = s[2:-2]\
        .replace("{", "")\
        .replace("}", "")

    counter = collections.Counter(
        map(int, s.split(","))
    )

    answer = [i for i,_ in counter.most_common()]

    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))