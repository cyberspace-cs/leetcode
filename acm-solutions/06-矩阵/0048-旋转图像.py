# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 48
标题 : 旋转图像
难度 : 中等
分类 : 矩阵
链接 : https://leetcode.cn/problems/rotate-image/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；随后 n 行，每行 n 个整数（n×n 方阵）。

【输出格式】
n 行，顺时针旋转 90° 后的矩阵。

【样例输入】
2
3
1 2 3
4 5 6
7 8 9
2
1 2
3 4

【样例输出】
7 4 1
8 5 2
9 6 3
3 1
4 2

"""

import sys


def solve(it):
    n = int(next(it))
    g = [[int(next(it)) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            g[i][j], g[j][i] = g[j][i], g[i][j]
    for row in g:
        row.reverse()
    return "\n".join(" ".join(map(str, row)) for row in g)

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
