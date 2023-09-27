def __find_path_sums__(tree, sum):
    sum += tree[0]
    if tree[1] is not None:
        tree1 = tree[1]
        sum1 = sum + tree1[0]
        if tree1[1] is not None:
            __find_path_sums__(tree1[1], sum1)
        if tree1[2] is not None:
            __find_path_sums__(tree1[2], sum1)
        if tree1[1] is None and tree1[2] is None:
            print(sum1)

    if tree[2] is not None:

        tree2 = tree[2]
        sum2 = sum + tree2[0]
        if tree2[1] is not None:
            __find_path_sums__(tree2[1], sum2)
        if tree2[2] is not None:
            __find_path_sums__(tree2[2], sum2)
        if tree2[1] is None and tree2[2] is None:
            print(sum2)

    if tree[1] is None and tree[2] is None:
        print(sum)


def find_path_sums(tree):
    sum = tree[0]

    if tree[1] is not None:
        __find_path_sums__(tree[1], sum)
    if tree[2] is not None:
        __find_path_sums__(tree[2], sum)
    if tree[1] is None and tree[2] is None:
        print(sum)
