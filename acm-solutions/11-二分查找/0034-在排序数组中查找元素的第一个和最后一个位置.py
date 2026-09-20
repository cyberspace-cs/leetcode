# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 34
标题 : 在排序数组中查找元素的第一个和最后一个位置
难度 : 中等
分类 : 二分查找
链接 : https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n target；第二行：n 个升序整数。

【输出格式】
一行，起始下标与结束下标（空格分隔）；不存在则输出 -1 -1。

【样例输入】
3
6 8
5 7 7 8 8 10
6 6
5 7 7 8 8 10
1 1
1

【样例输出】
3 4
-1 -1
0 0

"""

import sys


def solve(it):
    n = int(next(it))
    target = int(next(it))
    a = [int(next(it)) for _ in range(n)]

    def lower(x):
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo

    lo = lower(target)
    if lo == n or a[lo] != target:
        return "-1 -1"
    return "%d %d" % (lo, lower(target + 1) - 1)

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
