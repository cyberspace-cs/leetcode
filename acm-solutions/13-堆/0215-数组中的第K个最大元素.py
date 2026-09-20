# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 215
标题 : 数组中的第K个最大元素
难度 : 中等
分类 : 堆
链接 : https://leetcode.cn/problems/kth-largest-element-in-an-array/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n k；第二行：n 个整数。

【输出格式】
一行，第 k 个最大的元素（按排序位置计，不去重）。

【样例输入】
2
6 2
3 2 1 5 6 4
9 4
3 2 3 1 2 4 5 5 6

【样例输出】
5
4

"""

import sys


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
