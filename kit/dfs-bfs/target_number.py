from itertools import product

def solution(numbers, target):
    answer    = 0
    operators = [-1, 1]
    results   = []
    
    def calculate(operator_list):
        x = [n1*n2 for n1, n2 in zip(operator_list, numbers)]
        return sum(x)
    
    sets    = list(product(operators, repeat = len(numbers)))
    results = list(map(calculate, sets))
    
    return results.count(target)