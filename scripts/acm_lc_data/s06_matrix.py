# -*- coding: utf-8 -*-
"""矩阵分类 · 个人模板风格（单组输入）。"""

PROBLEMS = [
    dict(
        num=73, func='set_zeroes', params=[('matrix', 'List[List[int]]')], ret='List[List[int]]',
        body='''    # 在这里写你的代码（原地修改 matrix 后返回）
    m, n = len(matrix), len(matrix[0])
    rows = [False] * m
    cols = [False] * n
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows[i] = True
                cols[j] = True
    for i in range(m):
        for j in range(n):
            if rows[i] or cols[j]:
                matrix[i][j] = 0
    return matrix''',
        main='''    matrix = eval(input())
    print(set_zeroes(matrix))''',
        inp='一行：二维列表，如 [[1,1,1],[1,0,1],[1,1,1]]。',
        sample_in='[[1,1,1],[1,0,1],[1,1,1]]\n',
        sample_out='[[1, 0, 1], [0, 0, 0], [1, 0, 1]]\n',
    ),
    dict(
        num=54, func='spiral_order', params=[('matrix', 'List[List[int]]')], ret='List[int]',
        body='''    # 在这里写你的代码
    if not matrix:
        return []
    res = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            res.append(matrix[top][j])
        top += 1
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for j in range(right, left - 1, -1):
                res.append(matrix[bottom][j])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
    return res''',
        main='''    matrix = eval(input())
    print(spiral_order(matrix))''',
        inp='一行：二维列表，如 [[1,2,3],[4,5,6],[7,8,9]]。',
        sample_in='[[1,2,3],[4,5,6],[7,8,9]]\n',
        sample_out='[1, 2, 3, 6, 9, 8, 7, 4, 5]\n',
    ),
    dict(
        num=48, func='rotate_matrix', params=[('matrix', 'List[List[int]]')], ret='List[List[int]]',
        body='''    # 在这里写你的代码（原地旋转后返回）
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
    return matrix''',
        main='''    matrix = eval(input())
    print(rotate_matrix(matrix))''',
        inp='一行：n×n 二维列表，如 [[1,2,3],[4,5,6],[7,8,9]]。',
        sample_in='[[1,2,3],[4,5,6],[7,8,9]]\n',
        sample_out='[[7, 4, 1], [8, 5, 2], [9, 6, 3]]\n',
    ),
    dict(
        num=240, func='search_matrix', params=[('matrix', 'List[List[int]]'), ('target', 'int')], ret='bool',
        body='''    # 在这里写你的代码（从右上角出发）
    if not matrix:
        return False
    i, j = 0, len(matrix[0]) - 1
    while i < len(matrix) and j >= 0:
        if matrix[i][j] == target:
            return True
        if matrix[i][j] > target:
            j -= 1
        else:
            i += 1
    return False''',
        main='''    matrix = eval(input())
    target = int(input())
    print(search_matrix(matrix, target))''',
        inp='第一行：二维列表（每行每列均升序）；第二行：target。',
        sample_in='[[1,4,7],[2,5,8],[3,6,9]]\n5\n',
        sample_out='True\n',
    ),
]
