# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 31
标题 : 下一个排列
难度 : 中等
分类 : 技巧
链接 : https://leetcode.cn/problems/next-permutation/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个整数。

【输出格式】
一行，字典序中的下一个排列（若已是最大排列，则输出升序的最小排列）。

【样例输入】
3
3
1 2 3
3
3 2 1
3
1 1 5

【样例输出】
1 3 2
1 2 3
1 5 1

"""

import sys


def solve(it):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    i = n - 2
    while i >= 0 and a[i] >= a[i + 1]:
        i -= 1
    if i >= 0:
        j = n - 1
        while a[j] <= a[i]:
            j -= 1
        a[i], a[j] = a[j], a[i]
    a[i + 1:] = reversed(a[i + 1:])
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
