# -*- coding: utf-8 -*-
"""贪心算法分类的 ACM 模式完整解题。"""

PROBLEMS = [
    dict(
        num=121, title='买卖股票的最佳时机', difficulty='简单', category='贪心算法',
        slug='best-time-to-buy-and-sell-stock',
        inp='第一行：n；第二行：n 个整数表示每日股价。',
        outp='一行，只允许一次买卖的最大利润；不能获利则为 0。',
        sample_in='3\n6\n7 1 5 3 6 4\n5\n7 6 4 3 1\n1\n5\n',
        sample_out='5\n0\n0\n',
        code=r'''
def solve(it):
    n = int(next(it))
    prices = [int(next(it)) for _ in range(n)]
    low = prices[0]
    best = 0
    for p in prices[1:]:
        if p - low > best:
            best = p - low
        if p < low:
            low = p
    return best
''',
    ),
    dict(
        num=55, title='跳跃游戏', difficulty='中等', category='贪心算法', slug='jump-game',
        inp='第一行：n；第二行：n 个非负整数，表示每个位置能跳跃的最大长度。',
        outp='一行，true 或 false，表示能否到达最后一个位置。',
        sample_in='2\n5\n2 3 1 1 4\n5\n3 2 1 0 4\n',
        sample_out='true\nfalse\n',
        code=r'''
def solve(it):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    reach = 0
    for i in range(n):
        if i > reach:
            return "false"
        if i + a[i] > reach:
            reach = i + a[i]
    return "true"
''',
    ),
    dict(
        num=45, title='跳跃游戏 II', difficulty='中等', category='贪心算法', slug='jump-game-ii',
        inp='第一行：n；第二行：n 个非负整数（保证可以到达终点）。',
        outp='一行，到达最后一个位置的最少跳跃次数。',
        sample_in='2\n5\n2 3 1 1 4\n1\n1\n',
        sample_out='2\n0\n',
        code=r'''
def solve(it):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    jumps = 0
    cur_end = 0
    farthest = 0
    for i in range(n - 1):
        if i + a[i] > farthest:
            farthest = i + a[i]
        if i == cur_end:
            jumps += 1
            cur_end = farthest
    return jumps
''',
    ),
    dict(
        num=763, title='划分字母区间', difficulty='中等', category='贪心算法', slug='partition-labels',
        inp='一行：字符串 s（仅含小写字母）。',
        outp='一行，各片段长度（按出现顺序，空格分隔）。',
        sample_in='2\nababcbacadefegdehijhklij\nabc\n',
        sample_out='9 7 8\n1 1 1\n',
        code=r'''
def solve(it):
    s = next(it)
    last = {}
    for i, c in enumerate(s):
        last[c] = i
    res = []
    start = 0
    end = 0
    for i, c in enumerate(s):
        if last[c] > end:
            end = last[c]
        if i == end:
            res.append(end - start + 1)
            start = i + 1
    return " ".join(map(str, res))
''',
    ),
]
