# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 73
标题 : 矩阵置零
难度 : 中等
分类 : 矩阵
链接 : https://leetcode.cn/problems/set-matrix-zeroes/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：m n；随后 m 行，每行 n 个整数。

【输出格式】
m 行，置零后的矩阵。

【样例输入】
2
3 3
1 1 1
1 0 1
1 1 1
2 3
0 1 2
3 4 5

【样例输出】
1 0 1
0 0 0
1 0 1
0 0 0
0 4 5

"""

import sys


def solve(it):
    m = int(next(it))
    n = int(next(it))
    g = [[int(next(it)) for _ in range(n)] for _ in range(m)]
    rows = [False] * m
    cols = [False] * n
    for i in range(m):
        for j in range(n):
            if g[i][j] == 0:
                rows[i] = True
                cols[j] = True
    for i in range(m):
        for j in range(n):
            if rows[i] or cols[j]:
                g[i][j] = 0
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
