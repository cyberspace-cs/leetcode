# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 45
标题 : 跳跃游戏 II
难度 : 中等
分类 : 贪心算法
链接 : https://leetcode.cn/problems/jump-game-ii/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个非负整数（保证可以到达终点）。

【输出格式】
一行，到达最后一个位置的最少跳跃次数。

【样例输入】
2
5
2 3 1 1 4
1
1

【样例输出】
2
0

"""

import sys


def solve(it):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    jumps = 0
    cur_end = 0
    farthest = 0
    for i in range(n - 1):
        if i + a[i] > farthest:
            farthest = i + a[i]
        if i == cur_end:
            jumps += 1
            cur_end = farthest
    return jumps

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
