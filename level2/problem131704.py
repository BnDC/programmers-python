from typing import List


def solution(order: List) -> int:
    answer: int = 0
    n: int = len(order)

    belt = [n - i for i in range(n)]
    stack = []

    for o in order:
        if stack and stack[-1] == o:
            stack.pop()
            answer += 1
            continue

        while belt and belt[-1] != o:
            stack.append(belt.pop())
        if not belt:
            break
        else:
            belt.pop()
            answer += 1

    return answer


if __name__ == "__main__":
    print(solution([4, 3, 1, 2, 5]) == 2)
    print(solution([5, 4, 3, 2, 1]) == 5)
