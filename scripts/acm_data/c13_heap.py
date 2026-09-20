# -*- coding: utf-8 -*-
"""堆分类的 ACM 模式完整解题。"""

PROBLEMS = [
    dict(
        num=215, title='数组中的第K个最大元素', difficulty='中等', category='堆',
        slug='kth-largest-element-in-an-array',
        inp='第一行：n k；第二行：n 个整数。',
        outp='一行，第 k 个最大的元素（按排序位置计，不去重）。',
        sample_in='2\n6 2\n3 2 1 5 6 4\n9 4\n3 2 3 1 2 4 5 5 6\n',
        sample_out='5\n4\n',
        code=r'''
import heapq


def solve(it):
    n = int(next(it))
    k = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    h = []
    for x in a:
        heapq.heappush(h, x)
        if len(h) > k:
            heapq.heappop(h)
    return h[0]
''',
    ),
    dict(
        num=347, title='前 K 个高频元素', difficulty='中等', category='堆', slug='top-k-frequent-elements',
        inp='第一行：n k；第二行：n 个整数。',
        outp='一行，频率最高的 k 个元素（按频率降序，频率相同按值升序；空格分隔）。',
        sample_in='2\n6 2\n1 1 1 2 2 3\n1 1\n1\n',
        sample_out='1 2\n1\n',
        code=r'''
def solve(it):
    n = int(next(it))
    k = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    cnt = {}
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1
    items = sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))
    return " ".join(str(v) for v, _ in items[:k])
''',
    ),
    dict(
        num=295, title='数据流的中位数', difficulty='困难', category='堆', slug='find-median-from-data-stream',
        inp='第一行：q；随后 q 行，每行为 add num 或 findMedian。',
        outp='一行，按顺序输出所有 findMedian 的结果（整数原样输出，半整数保留 1 位小数，空格分隔）；\n'
             '若无查询则输出 EMPTY。',
        sample_in='2\n5\nadd 1\nadd 2\nfindMedian\nadd 3\nfindMedian\n4\nadd 6\nfindMedian\nadd 10\nfindMedian\n',
        sample_out='1.5 2\n6 8\n',
        code=r'''
import heapq


def solve(it):
    q = int(next(it))
    small = []
    large = []
    out = []
    for _ in range(q):
        op = next(it)
        if op == "add":
            x = int(next(it))
            heapq.heappush(small, -x)
            heapq.heappush(large, -heapq.heappop(small))
            if len(large) > len(small):
                heapq.heappush(small, -heapq.heappop(large))
        else:
            if len(small) > len(large):
                out.append(str(-small[0]))
            else:
                v = (-small[0] + large[0]) / 2.0
                out.append(str(int(v)) if v == int(v) else "%.1f" % v)
    return " ".join(out) if out else "EMPTY"
''',
    ),
]
