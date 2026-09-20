# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 739
标题 : 每日温度
难度 : 中等
分类 : 栈
链接 : https://leetcode.cn/problems/daily-temperatures/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个整数表示每日温度。

【输出格式】
一行，每天需要等待的天数（不会更高则为 0，空格分隔）。

【样例输入】
2
8
73 74 75 71 69 72 76 73
3
30 40 50

【样例输出】
1 1 4 2 1 1 0 0
1 1 0

"""

import sys


def solve(it):
    n = int(next(it))
    t = [int(next(it)) for _ in range(n)]
    res = [0] * n
    stack = []
    for i in range(n):
        while stack and t[i] > t[stack[-1]]:
            j = stack.pop()
            res[j] = i - j
        stack.append(i)
    return " ".join(map(str, res))

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
