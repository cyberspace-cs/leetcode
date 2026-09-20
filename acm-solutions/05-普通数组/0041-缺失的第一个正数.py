# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 41
标题 : 缺失的第一个正数
难度 : 困难
分类 : 普通数组
链接 : https://leetcode.cn/problems/first-missing-positive/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个整数。

【输出格式】
一行，未出现的最小正整数。

【样例输入】
3
3
1 2 0
4
3 4 -1 1
5
7 8 9 11 12

【样例输出】
3
2
1

"""

import sys


def solve(it):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    for i in range(n):
        while 1 <= a[i] <= n and a[a[i] - 1] != a[i]:
            j = a[i] - 1
            a[i], a[j] = a[j], a[i]
    for i in range(n):
        if a[i] != i + 1:
            return i + 1
    return n + 1

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
