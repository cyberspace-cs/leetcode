# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 189
标题 : 轮转数组
难度 : 中等
分类 : 普通数组
链接 : https://leetcode.cn/problems/rotate-array/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n k；第二行：n 个整数。向右轮转 k 步。

【输出格式】
一行，轮转后的数组（空格分隔）。

【样例输入】
2
7 3
1 2 3 4 5 6 7
4 2
-1 -100 3 99

【样例输出】
5 6 7 1 2 3 4
3 99 -1 -100

"""

import sys


def solve(it):
    n = int(next(it))
    k = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    if n:
        k %= n
        a.reverse()
        a[:k] = reversed(a[:k])
        a[k:] = reversed(a[k:])
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
