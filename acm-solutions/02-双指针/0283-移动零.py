# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 283
标题 : 移动零
难度 : 简单
分类 : 双指针
链接 : https://leetcode.cn/problems/move-zeroes/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个整数。

【输出格式】
一行，把 0 全部移到末尾后的数组（空格分隔）。

【样例输入】
2
5
0 1 0 3 12
1
0

【样例输出】
1 3 12 0 0
0

"""

import sys


def solve(it):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    k = 0
    for x in a:
        if x != 0:
            a[k] = x
            k += 1
    for i in range(k, n):
        a[i] = 0
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
