# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 089 / 100 题
================================================================
题号 : 322
标题 : 零钱兑换
难度 : 中等
分类 : 动态规划
链接 : https://leetcode.cn/problems/coin-change/
================================================================

【题目描述】
给定各种面额硬币（数量无限）和总金额，求凑出该金额所需的最少硬币数；无法凑出返回 -1。

【示例】
coins = [1,2,5], amount = 11  →  3   # 11 = 5 + 5 + 1

【思路提示】
完全背包：dp[j] = min(dp[j], dp[j - coin] + 1)，注意不可达状态用大数表示。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
