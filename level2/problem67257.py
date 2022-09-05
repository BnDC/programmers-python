import collections
import itertools
import re


def compute(nums, ops, idx) -> int:
    result = eval(nums[idx] + ops[idx] + nums[idx + 1])
    nums[idx] = str(result)
    nums.pop(idx + 1)
    ops.pop(idx)
    return result


def solution(expression):
    answer = 0
    nums = re.split('[+|\-|*]', expression)
    op_set = {"+", "-", "*"}
    operators = [e for e in expression if e in op_set]
    operator_counter = collections.Counter(operators)

    for permutation in itertools.permutations(op_set, 3):
        result = 0
        test_nums = nums[:]
        test_operators = operators[:]
        for op in permutation:
            cnt = operator_counter[op]
            while cnt:
                for i in range(len(test_operators)):
                    if op == test_operators[i]:
                        result += compute(test_nums, test_operators, i)
                        cnt -= 1
                        break
        answer = max(answer, abs(int(test_nums[0])))
    return answer


print(solution("100-200*300-500+20") == 60420)
print(solution("50*6-3*2") == 300)
