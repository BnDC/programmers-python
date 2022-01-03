def solution(n, m):
    if n >= m:
        big = n
        small = m
    else:
        big = m
        small = n

    while small != 0:  # or small != 1:
        i = 1
        mul = int()
        while mul < big:
            i += 1
            mul = small * i

        big, small = small, big-small*(i-1)

    return big, n*m//big
