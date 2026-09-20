# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 11
标题 : 盛最多水的容器
难度 : 中等
分类 : 双指针
链接 : https://leetcode.cn/problems/container-with-most-water/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个非负整数表示高度。

【输出格式】
一行，容器能盛的最大水量。

【样例输入】
2
9
1 8 6 2 5 4 8 3 7
2
1 1

【样例输出】
49
1

"""

import sys


def solve(it):
    n = int(next(it))
    h = [int(next(it)) for _ in range(n)]
    i, j, best = 0, n - 1, 0
    while i < j:
        area = min(h[i], h[j]) * (j - i)
        if area > best:
            best = area
        if h[i] < h[j]:
            i += 1
        else:
            j -= 1
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
