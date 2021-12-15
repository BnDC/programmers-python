def get_prime_number(num):
    if num == 1:
        return False

    elif num == 2:
        return True

    for i in range(3, num):
        if num % i == 0:
            return False

    return True


def solution(nums):
    answer = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                target = nums[i] + nums[j] + nums[k]

                if get_prime_number(target):
                    answer += 1

    return answer


print(get_prime_number(9))
print(solution([1, 2, 3, 4]))
print('\n')

print(solution([1, 2, 7, 6, 4]))
print('\n')

print(solution([1, 3, 5, 7, 9]))
# 9 11 13 13 15 17 15 17 19 21
print('\n')
