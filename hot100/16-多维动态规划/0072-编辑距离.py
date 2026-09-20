# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 094 / 100 题
================================================================
题号 : 72
标题 : 编辑距离
难度 : 中等
分类 : 多维动态规划
链接 : https://leetcode.cn/problems/edit-distance/
================================================================

【题目描述】
求把 word1 转换成 word2 所需的最少操作次数，允许插入、删除、替换一个字符。

【示例】
word1 = "horse", word2 = "ros"  →  3

【思路提示】
二维 DP，注意边界初始化（dp[0][j] = j、dp[i][0] = i），字符不同时取三种操作的最小值 + 1。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
