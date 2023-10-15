def solution(user_id, banned_id):
    user_len, banned_len = len(user_id), len(banned_id)
    answer = set()

    def dfs(cnt, r: int):
        if cnt == banned_len:
            answer.add(r)
            return

        for i in range(user_len):
            if (r & 1 << i) != 0: continue
            if is_matched(user_id[i], banned_id[cnt]):
                dfs(cnt + 1, r | 1 << i)

    result = 0
    for i in range(user_len):
        if is_matched(user_id[i], banned_id[0]):
            dfs(1, result | 1 << i)
    return len(answer)


def is_matched(w1: str, w2: str):
    if len(w1) != len(w2): return False
    for i in range(len(w1)):
        if w2[i] == '*': continue
        if w1[i] != w2[i]: return False
    return True


if __name__ == "__main__":
    # (lv3) problem64064 불량 사용자
    print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]) == 2)
    print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]) == 2)
    print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]) == 3)
