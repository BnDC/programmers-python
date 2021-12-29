def solution(sizes):
    answer = 0
    bigger_number_list = [size[0] if size[0] >=
                          size[1] else size[1] for size in sizes]
    smaller_number_list = [size[1] if size[0] >=
                           size[1] else size[0] for size in sizes]

    max_in_all = max(bigger_number_list)
    max_in_small = max(smaller_number_list)

    answer = max_in_all * max_in_small

    return answer
