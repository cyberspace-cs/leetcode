# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 090 / 100 题
================================================================
题号 : 416
标题 : 分割等和子集
难度 : 中等
分类 : 动态规划
链接 : https://leetcode.cn/problems/partition-equal-subset-sum/
================================================================

【题目描述】
判断能否把数组分割成两个元素和相等的子集。

【示例】
nums = [1,5,11,5]  →  true   # [1,5,5] 与 [11]

【思路提示】
01 背包：目标和为 sum/2，dp[j] 表示能否恰好凑出 j（倒序枚举容量）。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
