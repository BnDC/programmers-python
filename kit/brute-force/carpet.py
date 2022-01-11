#First
def seek_divisor(number):
    if number == 1:
        return [1]
    
    divisors = []
    divisor = 1
    i = 2
    
    while number != 1:
        if number % i == 0:
            divisor *= i
            divisors.append(divisor)
            divisors.append(number//i)
            number //= i
            i = 1
        i += 1

    return divisors

def solution(brown, yellow):
    answer          = []
    area            = brown + yellow
    yellow_divisors = seek_divisor(yellow)
    
    for divisor in yellow_divisors:
        if (divisor+2)*((yellow//divisor)+2) == area:
            answer = [(yellow//divisor)+2, divisor+2]
            
    answer.sort(reverse = True)
    
    return answer