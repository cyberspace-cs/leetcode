# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 84
标题 : 柱状图中最大的矩形
难度 : 困难
分类 : 栈
链接 : https://leetcode.cn/problems/largest-rectangle-in-histogram/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个非负整数表示柱子高度。

【输出格式】
一行，最大矩形面积。

【样例输入】
3
6
2 1 5 6 2 3
2
2 4
1
0

【样例输出】
10
4
0

"""

import sys


def solve(it):
    n = int(next(it))
    h = [int(next(it)) for _ in range(n)]
    h = h + [0]
    stack = []
    best = 0
    for i, x in enumerate(h):
        while stack and h[stack[-1]] > x:
            j = stack.pop()
            left = stack[-1] if stack else -1
            area = h[j] * (i - left - 1)
            if area > best:
                best = area
        stack.append(i)
    return best

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
