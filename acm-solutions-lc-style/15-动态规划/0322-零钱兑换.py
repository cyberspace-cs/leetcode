# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 322    标题: 零钱兑换    难度: 中等    分类: 动态规划
# 链接: https://leetcode.cn/problems/coin-change/
# 运行: python3 "0322-零钱兑换.py"   （按提示输入，或重定向样例输入）

def coin_change(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    # 在这里写你的代码
    INF = float("inf")
    dp = [0] + [INF] * amount
    for j in range(1, amount + 1):
        for c in coins:
            if c <= j and dp[j - c] + 1 < dp[j]:
                dp[j] = dp[j - c] + 1
    return dp[amount] if dp[amount] != INF else -1


def main():
    coins = eval(input())
    amount = int(input())
    print(coin_change(coins, amount))


if __name__ == "__main__":
    main()


# 322. 零钱兑换  中等
#
# 【题目描述】
# 给定各种面额硬币（数量无限）和总金额，求凑出该金额所需的最少硬币数；无法凑出返回 -1。
#
# 【示例】
# coins = [1,2,5], amount = 11  →  3   # 11 = 5 + 5 + 1
#
# 【思路提示】
# 完全背包：dp[j] = min(dp[j], dp[j - coin] + 1)，注意不可达状态用大数表示。
#
# 【输入格式】
# 第一行：硬币面额列表；第二行：amount。
#
# 【样例输入】
# [1,2,5]
# 11
# 【样例输出】
# 3
