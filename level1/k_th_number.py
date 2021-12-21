def solution(array, commands):
    answer = []

    for nums in commands:
        start = nums[0] - 1
        end = nums[1]
        k_th_index = nums[2] - 1

        sub_array = sorted(array[start:end])
        answer.append(sub_array[k_th_index])

    return answer
