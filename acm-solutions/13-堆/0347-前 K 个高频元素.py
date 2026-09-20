# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 347
标题 : 前 K 个高频元素
难度 : 中等
分类 : 堆
链接 : https://leetcode.cn/problems/top-k-frequent-elements/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n k；第二行：n 个整数。

【输出格式】
一行，频率最高的 k 个元素（按频率降序，频率相同按值升序；空格分隔）。

【样例输入】
2
6 2
1 1 1 2 2 3
1 1
1

【样例输出】
1 2
1

"""

import sys


def solve(it):
    n = int(next(it))
    k = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    cnt = {}
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1
    items = sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))
    return " ".join(str(v) for v, _ in items[:k])

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    t = int(next(it))
    out = []
    for _ in range(t):
        out.append(str(solve(it)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
