# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 322
标题 : 零钱兑换
难度 : 中等
分类 : 动态规划
链接 : https://leetcode.cn/problems/coin-change/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n amount；第二行：n 个硬币面额（可重复使用）。

【输出格式】
一行，凑出金额所需的最少硬币数；无法凑出输出 -1。

【样例输入】
3
3 11
1 2 5
1 3
2
2 3
1 2

【样例输出】
3
-1
2

"""

import sys


def solve(it):
    n = int(next(it))
    amount = int(next(it))
    coins = [int(next(it)) for _ in range(n)]
    INF = float("inf")
    dp = [0] + [INF] * amount
    for j in range(1, amount + 1):
        for c in coins:
            if c <= j and dp[j - c] + 1 < dp[j]:
                dp[j] = dp[j - c] + 1
    return dp[amount] if dp[amount] != INF else -1

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
