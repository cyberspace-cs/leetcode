# -*- coding: utf-8 -*-
"""二分查找分类的 ACM 模式完整解题。"""

PROBLEMS = [
    dict(
        num=35, title='搜索插入位置', difficulty='简单', category='二分查找', slug='search-insert-position',
        inp='第一行：n target；第二行：n 个升序整数。',
        outp='一行，目标值的下标；不存在则为应插入的位置。',
        sample_in='3\n4 5\n1 3 5 6\n4 2\n1 3 5 6\n4 7\n1 3 5 6\n',
        sample_out='2\n1\n4\n',
        code=r'''
def solve(it):
    n = int(next(it))
    target = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo
''',
    ),
    dict(
        num=74, title='搜索二维矩阵', difficulty='中等', category='二分查找', slug='search-a-2d-matrix',
        inp='第一行：m n target；随后 m 行，每行 n 个整数。\n'
            '矩阵满足每行升序，且每行首元素大于上一行末元素（整体可视为一维升序）。',
        outp='一行，true 或 false。',
        sample_in='3\n3 4 3\n1 3 5 7\n10 11 16 20\n23 30 34 60\n3 4 13\n1 3 5 7\n10 11 16 20\n23 30 34 60\n3 4 1\n1 3 5 7\n10 11 16 20\n23 30 34 60\n',
        sample_out='true\nfalse\ntrue\n',
        code=r'''
def solve(it):
    m = int(next(it))
    n = int(next(it))
    target = int(next(it))
    g = [[int(next(it)) for _ in range(n)] for _ in range(m)]
    lo, hi = 0, m * n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        v = g[mid // n][mid % n]
        if v == target:
            return "true"
        if v < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return "false"
''',
    ),
    dict(
        num=34, title='在排序数组中查找元素的第一个和最后一个位置', difficulty='中等', category='二分查找',
        slug='find-first-and-last-position-of-element-in-sorted-array',
        inp='第一行：n target；第二行：n 个升序整数。',
        outp='一行，起始下标与结束下标（空格分隔）；不存在则输出 -1 -1。',
        sample_in='3\n6 8\n5 7 7 8 8 10\n6 6\n5 7 7 8 8 10\n1 1\n1\n',
        sample_out='3 4\n-1 -1\n0 0\n',
        code=r'''
def solve(it):
    n = int(next(it))
    target = int(next(it))
    a = [int(next(it)) for _ in range(n)]

    def lower(x):
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo

    lo = lower(target)
    if lo == n or a[lo] != target:
        return "-1 -1"
    return "%d %d" % (lo, lower(target + 1) - 1)
''',
    ),
    dict(
        num=33, title='搜索旋转排序数组', difficulty='中等', category='二分查找', slug='search-in-rotated-sorted-array',
        inp='第一行：n target；第二行：n 个互不相同的整数（由升序数组旋转得到）。',
        outp='一行，目标值下标；不存在输出 -1。',
        sample_in='3\n7 0\n4 5 6 7 0 1 2\n7 3\n4 5 6 7 0 1 2\n1 3\n1\n',
        sample_out='4\n-1\n-1\n',
        code=r'''
def solve(it):
    n = int(next(it))
    target = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    lo, hi = 0, n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == target:
            return mid
        if a[lo] <= a[mid]:
            if a[lo] <= target < a[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if a[mid] < target <= a[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1
''',
    ),
    dict(
        num=153, title='寻找旋转排序数组中的最小值', difficulty='中等', category='二分查找',
        slug='find-minimum-in-rotated-sorted-array',
        inp='第一行：n；第二行：n 个互不相同的整数（由升序数组旋转得到）。',
        outp='一行，最小元素值。',
        sample_in='2\n5\n3 4 5 1 2\n4\n4 5 6 7\n',
        sample_out='1\n4\n',
        code=r'''
def solve(it):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    lo, hi = 0, n - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] > a[hi]:
            lo = mid + 1
        else:
            hi = mid
    return a[lo]
''',
    ),
    dict(
        num=4, title='寻找两个正序数组的中位数', difficulty='困难', category='二分查找',
        slug='median-of-two-sorted-arrays',
        inp='第一行：n；第二行：n 个升序整数；第三行：m；第四行：m 个升序整数。',
        outp='一行，中位数，保留 5 位小数。',
        sample_in='2\n2\n1 3\n1\n2\n2\n1 2\n2\n3 4\n',
        sample_out='2.00000\n2.50000\n',
        code=r'''
def solve(it):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    m = int(next(it))
    b = [int(next(it)) for _ in range(m)]
    if n > m:
        a, b, n, m = b, a, m, n
    total = n + m
    half = (total + 1) // 2
    lo, hi = 0, n
    while lo <= hi:
        i = (lo + hi) // 2
        j = half - i
        left_a = a[i - 1] if i > 0 else float("-inf")
        right_a = a[i] if i < n else float("inf")
        left_b = b[j - 1] if j > 0 else float("-inf")
        right_b = b[j] if j < m else float("inf")
        if left_a > right_b:
            hi = i - 1
        elif left_b > right_a:
            lo = i + 1
        else:
            if total % 2:
                return "%.5f" % max(left_a, left_b)
            return "%.5f" % ((max(left_a, left_b) + min(right_a, right_b)) / 2.0)
    return "0.00000"
''',
    ),
]
