import collections


def solution(begin, target, words):
    visited = []
    answer = []
    
    if target not in words:
        return 0

    def dfs(start, chars, cnt):
        if start in visited:
             return

        visited.append(start)

        if start == target:
            answer.append(cnt)
            return

        for char in chars:
            if len(set(start) - set(char)) == 1:
                after = chars[:]
                after.remove(char)
                cnt += 1
                dfs(char, after, cnt)
                cnt -= 1

    dfs(begin, words, 0)

    return min(answer)


# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))