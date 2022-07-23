def solution(skill, sill_trees):
    answer = 0
    graph = {s: [] for s in skill}

    for i in range(len(skill)):
        graph[skill[i]] = set(skill[:i])

    for skill_tree in sill_trees:
        is_True = True
        for i in range(len(skill_tree)):
            if skill_tree[i] not in graph:
                continue

            if not graph[skill_tree[i]].issubset(set(skill_tree[:i])):
                is_True = False
                break
        if is_True:
            answer += 1

    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))