# -*- coding: utf-8 -*-
"""哈希分类的 ACM 模式完整解题。"""

PROBLEMS = [
    dict(
        num=1, title='两数之和', difficulty='简单', category='哈希', slug='two-sum',
        inp='第一行：n target；第二行：n 个整数。',
        outp='一行，两个 0-based 下标（升序，空格分隔），保证有唯一解。',
        sample_in='2\n4 9\n2 7 11 15\n3 6\n3 2 4\n',
        sample_out='0 1\n1 2\n',
        code=r'''
def solve(it):
    n = int(next(it)); target = int(next(it))
    nums = [int(next(it)) for _ in range(n)]
    seen = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return "%d %d" % (seen[need], i)
        seen[x] = i
    return "-1 -1"
''',
    ),
    dict(
        num=49, title='字母异位词分组', difficulty='中等', category='哈希', slug='group-anagrams',
        inp='第一行：n；第二行：n 个仅含小写字母的字符串。',
        outp='第一行：组数 g；随后 g 行，每行一组，组内字符串按字典序升序、空格分隔；各组之间按行首字符串字典序升序。',
        sample_in='1\n6\neat tea tan ate nat bat\n',
        sample_out='3\nate eat tea\nbat\nnat tan\n',
        code=r'''
def solve(it):
    n = int(next(it))
    strs = [next(it) for _ in range(n)]
    groups = {}
    for s in strs:
        groups.setdefault("".join(sorted(s)), []).append(s)
    rows = []
    for g in groups.values():
        g.sort()
        rows.append(" ".join(g))
    rows.sort()
    return "\n".join([str(len(rows))] + rows)
''',
    ),
    dict(
        num=128, title='最长连续序列', difficulty='中等', category='哈希', slug='longest-consecutive-sequence',
        inp='第一行：n；第二行：n 个整数。',
        outp='一行，最长连续数字序列的长度。',
        sample_in='3\n6\n100 4 200 1 3 2\n4\n0 0 0 0\n5\n1 2 3 4 5\n',
        sample_out='4\n1\n5\n',
        code=r'''
def solve(it):
    n = int(next(it))
    nums = [int(next(it)) for _ in range(n)]
    pool = set(nums)
    best = 0
    for x in pool:
        if x - 1 in pool:
            continue
        y = x
        while y + 1 in pool:
            y += 1
        if y - x + 1 > best:
            best = y - x + 1
    return best
''',
    ),
]
