# -*- coding: utf-8 -*-
"""普通数组分类的 ACM 模式完整解题。"""

PROBLEMS = [
    dict(
        num=53, title='最大子数组和', difficulty='中等', category='普通数组', slug='maximum-subarray',
        inp='第一行：n；第二行：n 个整数。',
        outp='一行，最大连续子数组和。',
        sample_in='2\n9\n-2 1 -3 4 -1 2 1 -5 4\n1\n-1\n',
        sample_out='6\n-1\n',
        code=r'''
def solve(it):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    cur = best = a[0]
    for x in a[1:]:
        cur = x if cur < 0 else cur + x
        if cur > best:
            best = cur
    return best
''',
    ),
    dict(
        num=56, title='合并区间', difficulty='中等', category='普通数组', slug='merge-intervals',
        inp='第一行：n；随后 n 行，每行两个整数 l r 表示闭区间 [l, r]。',
        outp='第一行：合并后的区间数 g；随后 g 行，每行 l r（按左端点升序）。',
        sample_in='2\n4\n1 3\n2 6\n8 10\n15 18\n2\n1 4\n4 5\n',
        sample_out='3\n1 6\n8 10\n15 18\n1\n1 5\n',
        code=r'''
def solve(it):
    n = int(next(it))
    iv = []
    for _ in range(n):
        iv.append((int(next(it)), int(next(it))))
    iv.sort()
    res = []
    for l, r in iv:
        if res and l <= res[-1][1]:
            if r > res[-1][1]:
                res[-1][1] = r
        else:
            res.append([l, r])
    rows = ["%d %d" % (l, r) for l, r in res]
    return "\n".join([str(len(rows))] + rows)
''',
    ),
    dict(
        num=189, title='轮转数组', difficulty='中等', category='普通数组', slug='rotate-array',
        inp='第一行：n k；第二行：n 个整数。向右轮转 k 步。',
        outp='一行，轮转后的数组（空格分隔）。',
        sample_in='2\n7 3\n1 2 3 4 5 6 7\n4 2\n-1 -100 3 99\n',
        sample_out='5 6 7 1 2 3 4\n3 99 -1 -100\n',
        code=r'''
def solve(it):
    n = int(next(it))
    k = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    if n:
        k %= n
        a.reverse()
        a[:k] = reversed(a[:k])
        a[k:] = reversed(a[k:])
    return " ".join(map(str, a))
''',
    ),
    dict(
        num=238, title='除自身以外数组的乘积', difficulty='中等', category='普通数组',
        slug='product-of-array-except-self',
        inp='第一行：n；第二行：n 个整数。',
        outp='一行，answer[i] 为除 nums[i] 外其余元素的乘积。',
        sample_in='2\n4\n1 2 3 4\n5\n-1 1 0 -3 3\n',
        sample_out='24 12 8 6\n0 0 9 0 0\n',
        code=r'''
def solve(it):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    res = [1] * n
    p = 1
    for i in range(n):
        res[i] = p
        p *= a[i]
    p = 1
    for i in range(n - 1, -1, -1):
        res[i] *= p
        p *= a[i]
    return " ".join(map(str, res))
''',
    ),
    dict(
        num=41, title='缺失的第一个正数', difficulty='困难', category='普通数组', slug='first-missing-positive',
        inp='第一行：n；第二行：n 个整数。',
        outp='一行，未出现的最小正整数。',
        sample_in='3\n3\n1 2 0\n4\n3 4 -1 1\n5\n7 8 9 11 12\n',
        sample_out='3\n2\n1\n',
        code=r'''
def solve(it):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    for i in range(n):
        while 1 <= a[i] <= n and a[a[i] - 1] != a[i]:
            j = a[i] - 1
            a[i], a[j] = a[j], a[i]
    for i in range(n):
        if a[i] != i + 1:
            return i + 1
    return n + 1
''',
    ),
]
