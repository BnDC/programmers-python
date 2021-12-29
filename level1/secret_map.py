def solution(n, arr1, arr2):
    answer = []

    for e1, e2 in zip(arr1, arr2):

        e1_binary = bin(e1)[2:]
        e2_binary = bin(e2)[2:]

        e1_binary = '0' * (n-len(e1_binary)) + e1_binary
        e2_binary = '0' * (n-len(e2_binary)) + e2_binary

        print(e1_binary, e2_binary)
        temp = ''
        for l1, l2 in zip(e1_binary, e2_binary):
            if l1 == '1' or l2 == '1':
                temp += '#'
            else:
                temp += ' '

        answer.append(temp)

    return answer
