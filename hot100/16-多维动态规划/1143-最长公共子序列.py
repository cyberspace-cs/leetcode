# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 095 / 100 题
================================================================
题号 : 1143
标题 : 最长公共子序列
难度 : 中等
分类 : 多维动态规划
链接 : https://leetcode.cn/problems/longest-common-subsequence/
================================================================

【题目描述】
给定两个字符串，求它们的最长公共子序列的长度（子序列不必连续）。

【示例】
text1 = "abcde", text2 = "ace"  →  3   # "ace"

【思路提示】
dp[i][j]：字符相等则 dp[i-1][j-1] + 1，否则取 max(dp[i-1][j], dp[i][j-1])。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
