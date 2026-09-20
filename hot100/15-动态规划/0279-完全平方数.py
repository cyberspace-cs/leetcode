# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 087 / 100 题
================================================================
题号 : 279
标题 : 完全平方数
难度 : 中等
分类 : 动态规划
链接 : https://leetcode.cn/problems/perfect-squares/
================================================================

【题目描述】
求把 n 表示为若干个完全平方数之和所需的最少个数。

【示例】
n = 12  →  3   # 12 = 4 + 4 + 4

【思路提示】
完全背包 / BFS：dp[i] = min(dp[i - j*j] + 1)。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class Solution:
    def numSquares(self, n: int) -> int:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
