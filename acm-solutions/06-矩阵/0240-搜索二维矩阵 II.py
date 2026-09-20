# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 240
标题 : 搜索二维矩阵 II
难度 : 中等
分类 : 矩阵
链接 : https://leetcode.cn/problems/search-a-2d-matrix-ii/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：m n target；随后 m 行，每行 n 个整数（每行每列均升序）。

【输出格式】
一行，true 或 false。

【样例输入】
3
3 3 5
1 4 7
2 5 8
3 6 9
3 3 20
1 4 7
2 5 8
3 6 9
3 3 1
1 4 7
2 5 8
3 6 9

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
    i, j = 0, n - 1
    while i < m and j >= 0:
        if g[i][j] == target:
            return "true"
        if g[i][j] > target:
            j -= 1
        else:
            i += 1
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
