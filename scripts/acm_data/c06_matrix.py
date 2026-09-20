# -*- coding: utf-8 -*-
"""矩阵分类的 ACM 模式完整解题。"""

PROBLEMS = [
    dict(
        num=73, title='矩阵置零', difficulty='中等', category='矩阵', slug='set-matrix-zeroes',
        inp='第一行：m n；随后 m 行，每行 n 个整数。',
        outp='m 行，置零后的矩阵。',
        sample_in='2\n3 3\n1 1 1\n1 0 1\n1 1 1\n2 3\n0 1 2\n3 4 5\n',
        sample_out='1 0 1\n0 0 0\n1 0 1\n0 0 0\n0 4 5\n',
        code=r'''
def solve(it):
    m = int(next(it))
    n = int(next(it))
    g = [[int(next(it)) for _ in range(n)] for _ in range(m)]
    rows = [False] * m
    cols = [False] * n
    for i in range(m):
        for j in range(n):
            if g[i][j] == 0:
                rows[i] = True
                cols[j] = True
    for i in range(m):
        for j in range(n):
            if rows[i] or cols[j]:
                g[i][j] = 0
    return "\n".join(" ".join(map(str, row)) for row in g)
''',
    ),
    dict(
        num=54, title='螺旋矩阵', difficulty='中等', category='矩阵', slug='spiral-matrix',
        inp='第一行：m n；随后 m 行，每行 n 个整数。',
        outp='一行，按顺时针螺旋顺序遍历的元素（空格分隔）。',
        sample_in='2\n3 3\n1 2 3\n4 5 6\n7 8 9\n3 4\n1 2 3 4\n5 6 7 8\n9 10 11 12\n',
        sample_out='1 2 3 6 9 8 7 4 5\n1 2 3 4 8 12 11 10 9 5 6 7\n',
        code=r'''
def solve(it):
    m = int(next(it))
    n = int(next(it))
    g = [[int(next(it)) for _ in range(n)] for _ in range(m)]
    res = []
    top, bottom, left, right = 0, m - 1, 0, n - 1
    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            res.append(g[top][j])
        top += 1
        for i in range(top, bottom + 1):
            res.append(g[i][right])
        right -= 1
        if top <= bottom:
            for j in range(right, left - 1, -1):
                res.append(g[bottom][j])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(g[i][left])
            left += 1
    return " ".join(map(str, res))
''',
    ),
    dict(
        num=48, title='旋转图像', difficulty='中等', category='矩阵', slug='rotate-image',
        inp='第一行：n；随后 n 行，每行 n 个整数（n×n 方阵）。',
        outp='n 行，顺时针旋转 90° 后的矩阵。',
        sample_in='2\n3\n1 2 3\n4 5 6\n7 8 9\n2\n1 2\n3 4\n',
        sample_out='7 4 1\n8 5 2\n9 6 3\n3 1\n4 2\n',
        code=r'''
def solve(it):
    n = int(next(it))
    g = [[int(next(it)) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            g[i][j], g[j][i] = g[j][i], g[i][j]
    for row in g:
        row.reverse()
    return "\n".join(" ".join(map(str, row)) for row in g)
''',
    ),
    dict(
        num=240, title='搜索二维矩阵 II', difficulty='中等', category='矩阵', slug='search-a-2d-matrix-ii',
        inp='第一行：m n target；随后 m 行，每行 n 个整数（每行每列均升序）。',
        outp='一行，true 或 false。',
        sample_in='3\n3 3 5\n1 4 7\n2 5 8\n3 6 9\n3 3 20\n1 4 7\n2 5 8\n3 6 9\n3 3 1\n1 4 7\n2 5 8\n3 6 9\n',
        sample_out='true\nfalse\ntrue\n',
        code=r'''
def solve(it):
    m = int(next(it))
    n = int(next(it))
    target = int(next(it))
    g = [[int(next(it)) for _ in range(n)] for _ in range(m)]
    i, j = 0, n - 1
    while i < m and j >= 0:
        if g[i][j] == target:
            return "true"
        if g[i][j] > target:
            j -= 1
        else:
            i += 1
    return "false"
''',
    ),
]
