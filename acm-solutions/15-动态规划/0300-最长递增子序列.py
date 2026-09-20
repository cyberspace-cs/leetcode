# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 300
标题 : 最长递增子序列
难度 : 中等
分类 : 动态规划
链接 : https://leetcode.cn/problems/longest-increasing-subsequence/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个整数。

【输出格式】
一行，最长严格递增子序列的长度。

【样例输入】
2
8
10 9 2 5 3 7 101 18
4
7 7 7 7

【样例输出】
4
1

"""

import sys


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
