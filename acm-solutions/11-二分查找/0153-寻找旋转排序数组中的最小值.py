# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 153
标题 : 寻找旋转排序数组中的最小值
难度 : 中等
分类 : 二分查找
链接 : https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个互不相同的整数（由升序数组旋转得到）。

【输出格式】
一行，最小元素值。

【样例输入】
2
5
3 4 5 1 2
4
4 5 6 7

【样例输出】
1
4

"""

import sys


def solve(it):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    lo, hi = 0, n - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] > a[hi]:
            lo = mid + 1
        else:
            hi = mid
    return a[lo]

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
