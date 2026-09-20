# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 136
标题 : 只出现一次的数字
难度 : 简单
分类 : 技巧
链接 : https://leetcode.cn/problems/single-number/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个整数（除一个数字外，其余均出现两次）。

【输出格式】
一行，只出现一次的数字。

【样例输入】
2
5
4 1 2 1 2
3
2 2 1

【样例输出】
4
1

"""

import sys


def solve(it):
    n = int(next(it))
    x = 0
    for _ in range(n):
        x ^= int(next(it))
    return x

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
