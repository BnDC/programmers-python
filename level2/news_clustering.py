import collections


def solution(str1, str2):
    answer = 1

    # validate
    # 대소문자 구분 X, 영문자 아닌 글자 제외
    str1 = str1.lower()
    str2 = str2.lower()

    # 문제에서 알려준(?) 히든 케이스 교,합집합 모두 공집합일 경우
    # 자카드 유사도 구하기
    # 교집합 두 집합에서 그 원소가 등장 하는 빈도의 min값
    # 합집합 ~ max 값

    a = []
    b = []

    inter = 0
    union = 0

    for i in range(len(str1) - 1):
        tmp = str1[i: i+2]
        if tmp.isalpha():
            a.append(str1[i:i+2])

    for i in range(len(str2) - 1):
        tmp = str2[i: i+2]
        if tmp.isalpha():
            b.append(str2[i:i+2])

    counter_a = collections.Counter(a)
    counter_b = collections.Counter(b)

    # intersection
    for key in counter_a.keys():
        if counter_b.get(key) is not None:
            inter += min(counter_a[key], counter_b[key])

    # union
    for key in counter_a.keys():
        if counter_b.get(key) is None:
            union += counter_a[key]
        else:
            union += max(counter_a[key], counter_b[key])

    for key in counter_b.keys():
        if counter_a.get(key) is None:
            union += counter_b[key]

    if union == 0:
        answer *= 65536
    else:
        answer = int(inter/union*65536)

    return answer


print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))