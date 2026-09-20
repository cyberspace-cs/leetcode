# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 279
标题 : 完全平方数
难度 : 中等
分类 : 动态规划
链接 : https://leetcode.cn/problems/perfect-squares/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
一行：n。

【输出格式】
一行，表示 n 所需的最少完全平方数个数。

【样例输入】
3
12
13
1

【样例输出】
3
2
1

"""

import sys


def solve(it):
    n = int(next(it))
    dp = list(range(n + 1))
    for i in range(2, int(n ** 0.5) + 1):
        sq = i * i
        for j in range(sq, n + 1):
            if dp[j - sq] + 1 < dp[j]:
                dp[j] = dp[j - sq] + 1
    return dp[n]

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
