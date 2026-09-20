# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 42
标题 : 接雨水
难度 : 困难
分类 : 双指针
链接 : https://leetcode.cn/problems/trapping-rain-water/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个非负整数表示柱子高度。

【输出格式】
一行，能接住的雨水总量。

【样例输入】
2
12
0 1 0 2 1 0 1 3 2 1 2 1
3
4 2 3

【样例输出】
6
1

"""

import sys


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
