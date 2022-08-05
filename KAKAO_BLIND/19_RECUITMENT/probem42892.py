import sys

sys.setrecursionlimit(10 ** 6)  # 깊이 1000 넘는 테케 존재 6,7


def solution(nodeinfo):
    pre_order = []
    post_order = []

    tree = [[nodeinfo[i][0], nodeinfo[i][1], i + 1]
            for i in range(len(nodeinfo))]
    tree.sort(key=lambda x: x[0])

    def dfs(tree_list):
        if not tree_list:
            return
        max_y = 0  # root node의 y좌표
        max_idx = 0  # root node의 인덱스

        for i in range(len(tree_list)):
            if max_y < tree_list[i][1]:
                max_y = tree_list[i][1]
                max_idx = i

        pre_order.append(tree_list[max_idx][2])
        dfs(tree_list[:max_idx])
        dfs(tree_list[max_idx + 1:])
        post_order.append(tree_list[max_idx][2])

    dfs(tree)
    return [pre_order, post_order]


print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]) \
      == [[7, 4, 6, 9, 1, 8, 5, 2, 3], [9, 6, 5, 8, 1, 4, 3, 2, 7]])
