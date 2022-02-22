def solution(people, limit):
    people.sort()
    answer = 0
    left, right = 0, len(people) - 1

    while left <= right:
        answer += 1
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1

    return answer


# people = [50, 60, 70, 80]
# people = [50, 50, 60 ,70, 80]
# people = [10, 20, 30, 30]
people = [50, 50, 50, 50]
limit = 100

print(solution(people, limit))