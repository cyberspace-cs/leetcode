# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 198
标题 : 打家劫舍
难度 : 中等
分类 : 动态规划
链接 : https://leetcode.cn/problems/house-robber/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个非负整数表示每栋房屋金额。

【输出格式】
一行，能偷到的最大金额。

【样例输入】
3
4
1 2 3 1
5
2 7 9 3 1
1
5

【样例输出】
4
12
5

"""

import sys


def solve(it):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    prev = 0
    cur = 0
    for x in a:
        prev, cur = cur, max(cur, prev + x)
    return cur

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
