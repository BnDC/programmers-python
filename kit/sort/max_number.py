from itertools import permutations
from re import S

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers_permute = list(permutations(numbers, len(numbers)))
    # print(numbers_list)

    # for _ in range(len(numbers_permute)):
        # numbers_list.append()
    
    numbers_list = [int(''.join(number))  for number in numbers_permute]
    print(numbers_list)
    print(type(numbers_list[0]))


    return max(numbers_list) 

print(solution([6, 10 , 2]))