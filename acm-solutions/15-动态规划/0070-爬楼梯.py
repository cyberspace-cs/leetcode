# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 70
标题 : 爬楼梯
难度 : 简单
分类 : 动态规划
链接 : https://leetcode.cn/problems/climbing-stairs/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
一行：n，表示台阶数。

【输出格式】
一行，不同的爬法数量。

【样例输入】
3
3
1
5

【样例输出】
3
1
8

"""

import sys


def solve(it):
    n = int(next(it))
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a

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
