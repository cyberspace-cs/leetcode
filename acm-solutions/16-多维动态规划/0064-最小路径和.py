# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 64
标题 : 最小路径和
难度 : 中等
分类 : 多维动态规划
链接 : https://leetcode.cn/problems/minimum-path-sum/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：m n；随后 m 行，每行 n 个非负整数。

【输出格式】
一行，从左上角到右下角的最小路径和。

【样例输入】
2
3 3
1 3 1
1 5 1
4 2 1
2 3
1 2 3
4 5 6

【样例输出】
7
12

"""

import sys


def solve(it):
    m = int(next(it))
    n = int(next(it))
    g = [[int(next(it)) for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            up = g[i - 1][j] if i > 0 else None
            left = g[i][j - 1] if j > 0 else None
            if up is None:
                g[i][j] += left
            elif left is None:
                g[i][j] += up
            else:
                g[i][j] += min(up, left)
    return g[m - 1][n - 1]

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
