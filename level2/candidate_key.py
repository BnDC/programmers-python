import itertools


def solution(relation):
    answer = 0
    columns = list(range(len(relation[0])))
    # 0, 1, 2, ... , n
    candidate_keys = []

    # 갯수 1개 ~ n개 선택
    for i in range(1, len(relation) + 1):  # 1 ~ n
        # k개(1 ~ n) 뽑은 모든 경우의 수에 대해
        for com in itertools.combinations(columns, i):
            # 최소성 검사
            is_candidate_key = True # 이게 범인 ㅠㅠ
            for key in candidate_keys:
                if set(key).issubset(com):
                    is_candidate_key = False
                    break

            if not is_candidate_key:
                continue

            rows = []
            cardinality = True
            for rel in relation:
                row = [rel[i] for i in com]
                if row in rows:
                    cardinality = False
                    break
                rows.append(row)

            if cardinality:
                candidate_keys.append(com)

    return len(candidate_keys)


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))