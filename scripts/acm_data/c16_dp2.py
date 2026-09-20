# -*- coding: utf-8 -*-
"""多维动态规划分类的 ACM 模式完整解题。"""

PROBLEMS = [
    dict(
        num=62, title='不同路径', difficulty='中等', category='多维动态规划', slug='unique-paths',
        inp='一行：m n，表示 m×n 网格。',
        outp='一行，从左上角到右下角的不同路径数。',
        sample_in='3\n3 7\n3 2\n1 1\n',
        sample_out='28\n3\n1\n',
        code=r'''
def solve(it):
    m = int(next(it))
    n = int(next(it))
    dp = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[n - 1]
''',
    ),
    dict(
        num=64, title='最小路径和', difficulty='中等', category='多维动态规划', slug='minimum-path-sum',
        inp='第一行：m n；随后 m 行，每行 n 个非负整数。',
        outp='一行，从左上角到右下角的最小路径和。',
        sample_in='2\n3 3\n1 3 1\n1 5 1\n4 2 1\n2 3\n1 2 3\n4 5 6\n',
        sample_out='7\n12\n',
        code=r'''
def solve(it):
    m = int(next(it))
    n = int(next(it))
    g = [[int(next(it)) for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            up = g[i - 1][j] if i > 0 else None
            left = g[i][j - 1] if j > 0 else None
            if up is None:
                g[i][j] += left
            elif left is None:
                g[i][j] += up
            else:
                g[i][j] += min(up, left)
    return g[m - 1][n - 1]
''',
    ),
    dict(
        num=5, title='最长回文子串', difficulty='中等', category='多维动态规划', slug='longest-palindromic-substring',
        inp='一行：字符串 s（不含空白字符）。',
        outp='一行，最长回文子串（若存在多个等长答案，输出中心扩展过程中最先得到的那个）。',
        sample_in='3\nbabad\ncbbd\na\n',
        sample_out='bab\nbb\na\n',
        code=r'''
def solve(it):
    s = next(it)
    n = len(s)
    if n == 0:
        return "EMPTY"
    start, best = 0, 1
    for i in range(n):
        for l, r in ((i, i), (i, i + 1)):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            length = r - l - 1
            if length > best:
                best = length
                start = l + 1
    return s[start:start + best]
''',
    ),
    dict(
        num=1143, title='最长公共子序列', difficulty='中等', category='多维动态规划', slug='longest-common-subsequence',
        inp='第一行：字符串 text1；第二行：字符串 text2。',
        outp='一行，最长公共子序列的长度。',
        sample_in='3\nabcde\nace\nabc\nabc\naaa\naa\n',
        sample_out='3\n3\n2\n',
        code=r'''
def solve(it):
    a = next(it)
    b = next(it)
    n, m = len(a), len(b)
    dp = [0] * (m + 1)
    for i in range(1, n + 1):
        prev = 0
        for j in range(1, m + 1):
            tmp = dp[j]
            if a[i - 1] == b[j - 1]:
                dp[j] = prev + 1
            else:
                dp[j] = max(dp[j], dp[j - 1])
            prev = tmp
    return dp[m]
''',
    ),
    dict(
        num=72, title='编辑距离', difficulty='中等', category='多维动态规划', slug='edit-distance',
        inp='第一行：字符串 word1；第二行：字符串 word2。',
        outp='一行，最少操作次数（插入 / 删除 / 替换）。',
        sample_in='3\nhorse\nros\nintention\nexecution\nabc\nabc\n',
        sample_out='3\n5\n0\n',
        code=r'''
def solve(it):
    a = next(it)
    b = next(it)
    n, m = len(a), len(b)
    dp = list(range(m + 1))
    for i in range(1, n + 1):
        prev = dp[0]
        dp[0] = i
        for j in range(1, m + 1):
            tmp = dp[j]
            if a[i - 1] == b[j - 1]:
                dp[j] = prev
            else:
                dp[j] = 1 + min(prev, dp[j], dp[j - 1])
            prev = tmp
    return dp[m]
''',
    ),
]
