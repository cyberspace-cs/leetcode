# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 152
标题 : 乘积最大子数组
难度 : 中等
分类 : 动态规划
链接 : https://leetcode.cn/problems/maximum-product-subarray/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个整数。

【输出格式】
一行，乘积最大的连续子数组的乘积。

【样例输入】
3
4
2 3 -2 4
3
-2 0 -1
1
-3

【样例输出】
6
0
-3

"""

import sys


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
