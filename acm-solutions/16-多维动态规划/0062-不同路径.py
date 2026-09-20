# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 62
标题 : 不同路径
难度 : 中等
分类 : 多维动态规划
链接 : https://leetcode.cn/problems/unique-paths/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
一行：m n，表示 m×n 网格。

【输出格式】
一行，从左上角到右下角的不同路径数。

【样例输入】
3
3 7
3 2
1 1

【样例输出】
28
3
1

"""

import sys


def solve(it):
    m = int(next(it))
    n = int(next(it))
    dp = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[n - 1]

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
