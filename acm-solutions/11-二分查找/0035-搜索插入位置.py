# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 35
标题 : 搜索插入位置
难度 : 简单
分类 : 二分查找
链接 : https://leetcode.cn/problems/search-insert-position/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n target；第二行：n 个升序整数。

【输出格式】
一行，目标值的下标；不存在则为应插入的位置。

【样例输入】
3
4 5
1 3 5 6
4 2
1 3 5 6
4 7
1 3 5 6

【样例输出】
2
1
4

"""

import sys


def solve(it):
    n = int(next(it))
    target = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo

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
