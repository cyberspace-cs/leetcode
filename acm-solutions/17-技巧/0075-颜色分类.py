# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 75
标题 : 颜色分类
难度 : 中等
分类 : 技巧
链接 : https://leetcode.cn/problems/sort-colors/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个整数（仅含 0、1、2）。

【输出格式】
一行，按 0、1、2 顺序排列后的数组（空格分隔）。

【样例输入】
2
6
2 0 2 1 1 0
3
2 1 0

【样例输出】
0 0 1 1 2 2
0 1 2

"""

import sys


def solve(it):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    p0, i, p2 = 0, 0, n - 1
    while i <= p2:
        if a[i] == 0:
            a[p0], a[i] = a[i], a[p0]
            p0 += 1
            i += 1
        elif a[i] == 2:
            a[i], a[p2] = a[p2], a[i]
            p2 -= 1
        else:
            i += 1
    return " ".join(map(str, a))

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
