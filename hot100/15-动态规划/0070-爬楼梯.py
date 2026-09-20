# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 082 / 100 题
================================================================
题号 : 70
标题 : 爬楼梯
难度 : 简单
分类 : 动态规划
链接 : https://leetcode.cn/problems/climbing-stairs/
================================================================

【题目描述】
每次可以爬 1 或 2 个台阶，求爬到第 n 阶有多少种不同的方法。

【示例】
n = 3  →  3   # 1+1+1 / 1+2 / 2+1

【思路提示】
dp[i] = dp[i-1] + dp[i-2]，可用两个滚动变量把空间优化到 O(1)。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class Solution:
    def climbStairs(self, n: int) -> int:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
