# -*- coding: utf-8 -*-
"""双指针分类的 ACM 模式完整解题。"""

PROBLEMS = [
    dict(
        num=283, title='移动零', difficulty='简单', category='双指针', slug='move-zeroes',
        inp='第一行：n；第二行：n 个整数。',
        outp='一行，把 0 全部移到末尾后的数组（空格分隔）。',
        sample_in='2\n5\n0 1 0 3 12\n1\n0\n',
        sample_out='1 3 12 0 0\n0\n',
        code=r'''
def solve(it):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    k = 0
    for x in a:
        if x != 0:
            a[k] = x
            k += 1
    for i in range(k, n):
        a[i] = 0
    return " ".join(map(str, a))
''',
    ),
    dict(
        num=11, title='盛最多水的容器', difficulty='中等', category='双指针', slug='container-with-most-water',
        inp='第一行：n；第二行：n 个非负整数表示高度。',
        outp='一行，容器能盛的最大水量。',
        sample_in='2\n9\n1 8 6 2 5 4 8 3 7\n2\n1 1\n',
        sample_out='49\n1\n',
        code=r'''
def solve(it):
    n = int(next(it))
    h = [int(next(it)) for _ in range(n)]
    i, j, best = 0, n - 1, 0
    while i < j:
        area = min(h[i], h[j]) * (j - i)
        if area > best:
            best = area
        if h[i] < h[j]:
            i += 1
        else:
            j -= 1
    return best
''',
    ),
    dict(
        num=15, title='三数之和', difficulty='中等', category='双指针', slug='3sum',
        inp='第一行：n；第二行：n 个整数。',
        outp='第一行：方案数 g；随后 g 行，每行三个升序整数（空格分隔），整体按字典序升序；无解时仅输出 0。',
        sample_in='2\n6\n-1 0 1 2 -1 -4\n3\n0 1 1\n',
        sample_out='2\n-1 -1 2\n-1 0 1\n0\n',
        code=r'''
def solve(it):
    n = int(next(it))
    nums = sorted(int(next(it)) for _ in range(n))
    res = []
    for i in range(n - 2):
        if i and nums[i] == nums[i - 1]:
            continue
        if nums[i] > 0:
            break
        l, r = i + 1, n - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
    rows = ["%d %d %d" % t for t in res]
    return "\n".join([str(len(rows))] + rows)
''',
    ),
    dict(
        num=42, title='接雨水', difficulty='困难', category='双指针', slug='trapping-rain-water',
        inp='第一行：n；第二行：n 个非负整数表示柱子高度。',
        outp='一行，能接住的雨水总量。',
        sample_in='2\n12\n0 1 0 2 1 0 1 3 2 1 2 1\n3\n4 2 3\n',
        sample_out='6\n1\n',
        code=r'''
def solve(it):
    n = int(next(it))
    h = [int(next(it)) for _ in range(n)]
    l, r = 0, n - 1
    lmax = rmax = 0
    ans = 0
    while l < r:
        if h[l] < h[r]:
            if h[l] > lmax:
                lmax = h[l]
            ans += lmax - h[l]
            l += 1
        else:
            if h[r] > rmax:
                rmax = h[r]
            ans += rmax - h[r]
            r -= 1
    return ans
''',
    ),
]
