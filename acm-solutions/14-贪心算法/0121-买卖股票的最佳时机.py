# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 121
标题 : 买卖股票的最佳时机
难度 : 简单
分类 : 贪心算法
链接 : https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个整数表示每日股价。

【输出格式】
一行，只允许一次买卖的最大利润；不能获利则为 0。

【样例输入】
3
6
7 1 5 3 6 4
5
7 6 4 3 1
1
5

【样例输出】
5
0
0

"""

import sys


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
