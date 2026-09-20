# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 74
标题 : 搜索二维矩阵
难度 : 中等
分类 : 二分查找
链接 : https://leetcode.cn/problems/search-a-2d-matrix/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：m n target；随后 m 行，每行 n 个整数。
矩阵满足每行升序，且每行首元素大于上一行末元素（整体可视为一维升序）。

【输出格式】
一行，true 或 false。

【样例输入】
3
3 4 3
1 3 5 7
10 11 16 20
23 30 34 60
3 4 13
1 3 5 7
10 11 16 20
23 30 34 60
3 4 1
1 3 5 7
10 11 16 20
23 30 34 60

【样例输出】
true
false
true

"""

import sys


def solve(it):
    m = int(next(it))
    n = int(next(it))
    target = int(next(it))
    g = [[int(next(it)) for _ in range(n)] for _ in range(m)]
    lo, hi = 0, m * n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        v = g[mid // n][mid % n]
        if v == target:
            return "true"
        if v < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return "false"

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
