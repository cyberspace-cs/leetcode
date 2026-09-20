# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 54
标题 : 螺旋矩阵
难度 : 中等
分类 : 矩阵
链接 : https://leetcode.cn/problems/spiral-matrix/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：m n；随后 m 行，每行 n 个整数。

【输出格式】
一行，按顺时针螺旋顺序遍历的元素（空格分隔）。

【样例输入】
2
3 3
1 2 3
4 5 6
7 8 9
3 4
1 2 3 4
5 6 7 8
9 10 11 12

【样例输出】
1 2 3 6 9 8 7 4 5
1 2 3 4 8 12 11 10 9 5 6 7

"""

import sys


def solve(it):
    m = int(next(it))
    n = int(next(it))
    g = [[int(next(it)) for _ in range(n)] for _ in range(m)]
    res = []
    top, bottom, left, right = 0, m - 1, 0, n - 1
    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            res.append(g[top][j])
        top += 1
        for i in range(top, bottom + 1):
            res.append(g[i][right])
        right -= 1
        if top <= bottom:
            for j in range(right, left - 1, -1):
                res.append(g[bottom][j])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(g[i][left])
            left += 1
    return " ".join(map(str, res))

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
