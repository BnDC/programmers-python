def solution(queue1, queue2):
    q = queue1 + queue2
    left, right = 0, len(queue1) - 1

    answer, cur = 0, 0
    cur = sum(queue1) - q[right]
    target = sum(q) // 2

    while right < len(q):
        if cur == target:
            return answer - 1
        elif cur < target:
            cur += q[right]
            right += 1
        else:
            cur -= q[left]
            left += 1
        answer += 1
    return -1


print(solution([3, 2, 7, 2], [4, 6, 5, 1]) == 2)
print(solution([1, 2, 1, 2], [1, 10, 1, 2]) == 7)
print(solution([1, 1], [1, 5]) == -1ㅑ)