# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 4
标题 : 寻找两个正序数组的中位数
难度 : 困难
分类 : 二分查找
链接 : https://leetcode.cn/problems/median-of-two-sorted-arrays/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个升序整数；第三行：m；第四行：m 个升序整数。

【输出格式】
一行，中位数，保留 5 位小数。

【样例输入】
2
2
1 3
1
2
2
1 2
2
3 4

【样例输出】
2.00000
2.50000

"""

import sys


def solve(it):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    m = int(next(it))
    b = [int(next(it)) for _ in range(m)]
    if n > m:
        a, b, n, m = b, a, m, n
    total = n + m
    half = (total + 1) // 2
    lo, hi = 0, n
    while lo <= hi:
        i = (lo + hi) // 2
        j = half - i
        left_a = a[i - 1] if i > 0 else float("-inf")
        right_a = a[i] if i < n else float("inf")
        left_b = b[j - 1] if j > 0 else float("-inf")
        right_b = b[j] if j < m else float("inf")
        if left_a > right_b:
            hi = i - 1
        elif left_b > right_a:
            lo = i + 1
        else:
            if total % 2:
                return "%.5f" % max(left_a, left_b)
            return "%.5f" % ((max(left_a, left_b) + min(right_a, right_b)) / 2.0)
    return "0.00000"

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
