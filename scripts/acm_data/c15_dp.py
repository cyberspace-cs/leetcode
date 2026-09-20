# -*- coding: utf-8 -*-
"""动态规划分类的 ACM 模式完整解题。"""

PROBLEMS = [
    dict(
        num=70, title='爬楼梯', difficulty='简单', category='动态规划', slug='climbing-stairs',
        inp='一行：n，表示台阶数。',
        outp='一行，不同的爬法数量。',
        sample_in='3\n3\n1\n5\n',
        sample_out='3\n1\n8\n',
        code=r'''
def solve(it):
    n = int(next(it))
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a
''',
    ),
    dict(
        num=118, title='杨辉三角', difficulty='简单', category='动态规划', slug='pascals-triangle',
        inp='一行：numRows，表示行数。',
        outp='numRows 行，每行该行的数字（空格分隔）。',
        sample_in='1\n5\n',
        sample_out='1\n1 1\n1 2 1\n1 3 3 1\n1 4 6 4 1\n',
        code=r'''
def solve(it):
    n = int(next(it))
    rows = []
    cur = []
    for _ in range(n):
        cur = [1] + [cur[i] + cur[i + 1] for i in range(len(cur) - 1)] + [1] if cur else [1]
        rows.append(" ".join(map(str, cur)))
    return "\n".join(rows) if rows else "EMPTY"
''',
    ),
    dict(
        num=198, title='打家劫舍', difficulty='中等', category='动态规划', slug='house-robber',
        inp='第一行：n；第二行：n 个非负整数表示每栋房屋金额。',
        outp='一行，能偷到的最大金额。',
        sample_in='3\n4\n1 2 3 1\n5\n2 7 9 3 1\n1\n5\n',
        sample_out='4\n12\n5\n',
        code=r'''
def solve(it):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    prev = 0
    cur = 0
    for x in a:
        prev, cur = cur, max(cur, prev + x)
    return cur
''',
    ),
    dict(
        num=279, title='完全平方数', difficulty='中等', category='动态规划', slug='perfect-squares',
        inp='一行：n。',
        outp='一行，表示 n 所需的最少完全平方数个数。',
        sample_in='3\n12\n13\n1\n',
        sample_out='3\n2\n1\n',
        code=r'''
def solve(it):
    n = int(next(it))
    dp = list(range(n + 1))
    for i in range(2, int(n ** 0.5) + 1):
        sq = i * i
        for j in range(sq, n + 1):
            if dp[j - sq] + 1 < dp[j]:
                dp[j] = dp[j - sq] + 1
    return dp[n]
''',
    ),
    dict(
        num=322, title='零钱兑换', difficulty='中等', category='动态规划', slug='coin-change',
        inp='第一行：n amount；第二行：n 个硬币面额（可重复使用）。',
        outp='一行，凑出金额所需的最少硬币数；无法凑出输出 -1。',
        sample_in='3\n3 11\n1 2 5\n1 3\n2\n2 3\n1 2\n',
        sample_out='3\n-1\n2\n',
        code=r'''
def solve(it):
    n = int(next(it))
    amount = int(next(it))
    coins = [int(next(it)) for _ in range(n)]
    INF = float("inf")
    dp = [0] + [INF] * amount
    for j in range(1, amount + 1):
        for c in coins:
            if c <= j and dp[j - c] + 1 < dp[j]:
                dp[j] = dp[j - c] + 1
    return dp[amount] if dp[amount] != INF else -1
''',
    ),
    dict(
        num=139, title='单词拆分', difficulty='中等', category='动态规划', slug='word-break',
        inp='第一行：字符串 s；第二行：k；第三行：k 个单词。',
        outp='一行，true 或 false。',
        sample_in='3\nleetcode\n2\nleet code\napplepenapple\n2\napple pen\ncatsandog\n5\ncats dog sand and cat\n',
        sample_out='true\ntrue\nfalse\n',
        code=r'''
def solve(it):
    s = next(it)
    k = int(next(it))
    words = set(next(it) for _ in range(k))
    n = len(s)
    maxlen = max((len(w) for w in words), default=0)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(max(0, i - maxlen), i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return "true" if dp[n] else "false"
''',
    ),
    dict(
        num=300, title='最长递增子序列', difficulty='中等', category='动态规划', slug='longest-increasing-subsequence',
        inp='第一行：n；第二行：n 个整数。',
        outp='一行，最长严格递增子序列的长度。',
        sample_in='2\n8\n10 9 2 5 3 7 101 18\n4\n7 7 7 7\n',
        sample_out='4\n1\n',
        code=r'''
import bisect


def solve(it):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    tails = []
    for x in a:
        i = bisect.bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)
''',
    ),
    dict(
        num=152, title='乘积最大子数组', difficulty='中等', category='动态规划', slug='maximum-product-subarray',
        inp='第一行：n；第二行：n 个整数。',
        outp='一行，乘积最大的连续子数组的乘积。',
        sample_in='3\n4\n2 3 -2 4\n3\n-2 0 -1\n1\n-3\n',
        sample_out='6\n0\n-3\n',
        code=r'''
def solve(it):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    hi = lo = best = a[0]
    for x in a[1:]:
        if x < 0:
            hi, lo = lo, hi
        hi = max(x, hi * x)
        lo = min(x, lo * x)
        if hi > best:
            best = hi
    return best
''',
    ),
    dict(
        num=416, title='分割等和子集', difficulty='中等', category='动态规划', slug='partition-equal-subset-sum',
        inp='第一行：n；第二行：n 个正整数。',
        outp='一行，true 或 false。',
        sample_in='3\n4\n1 5 11 5\n4\n1 2 3 5\n1\n2\n',
        sample_out='true\nfalse\nfalse\n',
        code=r'''
def solve(it):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    total = sum(a)
    if total % 2:
        return "false"
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for x in a:
        for j in range(target, x - 1, -1):
            if dp[j - x]:
                dp[j] = True
    return "true" if dp[target] else "false"
''',
    ),
    dict(
        num=32, title='最长有效括号', difficulty='困难', category='动态规划', slug='longest-valid-parentheses',
        inp='一行：字符串 s（仅含左右括号）。',
        outp='一行，最长有效括号子串的长度。',
        sample_in='3\n(()\n)()())\n()(())\n',
        sample_out='2\n4\n6\n',
        code=r'''
def solve(it):
    s = next(it)
    n = len(s)
    dp = [0] * n
    best = 0
    for i in range(1, n):
        if s[i] != ")":
            continue
        if s[i - 1] == "(":
            dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
        else:
            j = i - dp[i - 1] - 1
            if j >= 0 and s[j] == "(":
                dp[i] = dp[i - 1] + 2 + (dp[j - 1] if j >= 1 else 0)
        if dp[i] > best:
            best = dp[i]
    return best
''',
    ),
]
