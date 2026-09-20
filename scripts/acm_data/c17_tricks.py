# -*- coding: utf-8 -*-
"""技巧分类的 ACM 模式完整解题。"""

PROBLEMS = [
    dict(
        num=136, title='只出现一次的数字', difficulty='简单', category='技巧', slug='single-number',
        inp='第一行：n；第二行：n 个整数（除一个数字外，其余均出现两次）。',
        outp='一行，只出现一次的数字。',
        sample_in='2\n5\n4 1 2 1 2\n3\n2 2 1\n',
        sample_out='4\n1\n',
        code=r'''
def solve(it):
    n = int(next(it))
    x = 0
    for _ in range(n):
        x ^= int(next(it))
    return x
''',
    ),
    dict(
        num=169, title='多数元素', difficulty='简单', category='技巧', slug='majority-element',
        inp='第一行：n；第二行：n 个整数（保证存在出现次数 > n/2 的元素）。',
        outp='一行，多数元素。',
        sample_in='2\n7\n2 2 1 1 1 2 2\n3\n3 2 3\n',
        sample_out='2\n3\n',
        code=r'''
def solve(it):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    cand = None
    count = 0
    for x in a:
        if count == 0:
            cand = x
            count = 1
        elif x == cand:
            count += 1
        else:
            count -= 1
    return cand
''',
    ),
    dict(
        num=75, title='颜色分类', difficulty='中等', category='技巧', slug='sort-colors',
        inp='第一行：n；第二行：n 个整数（仅含 0、1、2）。',
        outp='一行，按 0、1、2 顺序排列后的数组（空格分隔）。',
        sample_in='2\n6\n2 0 2 1 1 0\n3\n2 1 0\n',
        sample_out='0 0 1 1 2 2\n0 1 2\n',
        code=r'''
def solve(it):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    p0, i, p2 = 0, 0, n - 1
    while i <= p2:
        if a[i] == 0:
            a[p0], a[i] = a[i], a[p0]
            p0 += 1
            i += 1
        elif a[i] == 2:
            a[i], a[p2] = a[p2], a[i]
            p2 -= 1
        else:
            i += 1
    return " ".join(map(str, a))
''',
    ),
    dict(
        num=31, title='下一个排列', difficulty='中等', category='技巧', slug='next-permutation',
        inp='第一行：n；第二行：n 个整数。',
        outp='一行，字典序中的下一个排列（若已是最大排列，则输出升序的最小排列）。',
        sample_in='3\n3\n1 2 3\n3\n3 2 1\n3\n1 1 5\n',
        sample_out='1 3 2\n1 2 3\n1 5 1\n',
        code=r'''
def solve(it):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    i = n - 2
    while i >= 0 and a[i] >= a[i + 1]:
        i -= 1
    if i >= 0:
        j = n - 1
        while a[j] <= a[i]:
            j -= 1
        a[i], a[j] = a[j], a[i]
    a[i + 1:] = reversed(a[i + 1:])
    return " ".join(map(str, a))
''',
    ),
    dict(
        num=287, title='寻找重复数', difficulty='中等', category='技巧', slug='find-the-duplicate-number',
        inp='第一行：n；第二行：n 个整数（取值在 1..n-1 之间，仅有一个数字重复）。',
        outp='一行，重复的数字。',
        sample_in='2\n5\n1 3 4 2 2\n6\n3 1 3 4 2 5\n',
        sample_out='2\n3\n',
        code=r'''
def solve(it):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    slow = fast = a[0]
    while True:
        slow = a[slow]
        fast = a[a[fast]]
        if slow == fast:
            break
    slow = a[0]
    while slow != fast:
        slow = a[slow]
        fast = a[fast]
    return slow
''',
    ),
]
