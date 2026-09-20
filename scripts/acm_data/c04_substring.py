# -*- coding: utf-8 -*-
"""子串分类的 ACM 模式完整解题。"""

PROBLEMS = [
    dict(
        num=560, title='和为 K 的子数组', difficulty='中等', category='子串', slug='subarray-sum-equals-k',
        inp='第一行：n k；第二行：n 个整数。',
        outp='一行，和为 k 的连续子数组个数。',
        sample_in='3\n3 2\n1 1 1\n3 3\n1 2 3\n4 0\n0 0 0 0\n',
        sample_out='2\n2\n10\n',
        code=r'''
def solve(it):
    n = int(next(it))
    k = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    cnt = {0: 1}
    pre = 0
    ans = 0
    for x in a:
        pre += x
        ans += cnt.get(pre - k, 0)
        cnt[pre] = cnt.get(pre, 0) + 1
    return ans
''',
    ),
    dict(
        num=239, title='滑动窗口最大值', difficulty='困难', category='子串', slug='sliding-window-maximum',
        inp='第一行：n k；第二行：n 个整数。窗口每次右移一位，共 n-k+1 个窗口。',
        outp='一行，每个窗口的最大值（空格分隔）。',
        sample_in='2\n8 3\n1 3 -1 -3 5 3 6 7\n1 1\n5\n',
        sample_out='3 3 5 5 6 7\n5\n',
        code=r'''
from collections import deque


def solve(it):
    n = int(next(it))
    k = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    dq = deque()
    res = []
    for i, x in enumerate(a):
        while dq and a[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            res.append(a[dq[0]])
    return " ".join(map(str, res))
''',
    ),
    dict(
        num=76, title='最小覆盖子串', difficulty='困难', category='子串', slug='minimum-window-substring',
        inp='第一行：字符串 s；第二行：字符串 t（均不含空白字符）。',
        outp='一行，s 中涵盖 t 全部字符的最短子串；不存在则输出 -1。',
        sample_in='2\nADOBECODEBANC\nABC\na\naa\n',
        sample_out='BANC\n-1\n',
        code=r'''
def solve(it):
    s = next(it)
    t = next(it)
    need = {}
    for c in t:
        need[c] = need.get(c, 0) + 1
    missing = len(t)
    left = 0
    best = None
    for right, c in enumerate(s):
        if need.get(c, 0) > 0:
            missing -= 1
        need[c] = need.get(c, 0) - 1
        while missing == 0:
            if best is None or right - left + 1 < best[1] - best[0] + 1:
                best = (left, right)
            need[s[left]] = need.get(s[left], 0) + 1
            if need[s[left]] > 0:
                missing += 1
            left += 1
    return s[best[0]:best[1] + 1] if best else "-1"
''',
    ),
]
