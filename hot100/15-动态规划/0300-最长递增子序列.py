# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 088 / 100 题
================================================================
题号 : 300
标题 : 最长递增子序列
难度 : 中等
分类 : 动态规划
链接 : https://leetcode.cn/problems/longest-increasing-subsequence/
================================================================

【题目描述】
求数组中最长严格递增子序列的长度（子序列不必连续）。

【示例】
nums = [10,9,2,5,3,7,101,18]  →  4   # [2,3,7,101]

【思路提示】
O(n²) 的 DP 定义；进阶用「贪心 + 二分」维护长度为 L 的最小结尾值，做到 O(n log n)。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
