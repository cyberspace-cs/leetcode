# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 012 / 100 题
================================================================
题号 : 560
标题 : 和为 K 的子数组
难度 : 中等
分类 : 子串
链接 : https://leetcode.cn/problems/subarray-sum-equals-k/
================================================================

【题目描述】
统计数组中和恰好为 k 的连续子数组的个数（元素可含负数）。

【示例】
nums = [1,1,1], k = 2  →  2

【思路提示】
前缀和 + 哈希表计数：遍历时累加前缀和，查询 (前缀和 - k) 出现过几次。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
