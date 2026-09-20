# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 55
标题 : 跳跃游戏
难度 : 中等
分类 : 贪心算法
链接 : https://leetcode.cn/problems/jump-game/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个非负整数，表示每个位置能跳跃的最大长度。

【输出格式】
一行，true 或 false，表示能否到达最后一个位置。

【样例输入】
2
5
2 3 1 1 4
5
3 2 1 0 4

【样例输出】
true
false

"""

import sys


def solve(it):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    reach = 0
    for i in range(n):
        if i > reach:
            return "false"
        if i + a[i] > reach:
            reach = i + a[i]
    return "true"

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
