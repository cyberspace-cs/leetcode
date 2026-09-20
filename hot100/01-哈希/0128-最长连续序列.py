# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 003 / 100 题
================================================================
题号 : 128
标题 : 最长连续序列
难度 : 中等
分类 : 哈希
链接 : https://leetcode.cn/problems/longest-consecutive-sequence/
================================================================

【题目描述】
给定未排序整数数组 nums，找出数字连续的最长序列长度，要求算法时间复杂度 O(n)。

【示例】
nums = [100,4,200,1,3,2]  →  4   # 最长连续序列为 1,2,3,4

【思路提示】
全部放入集合，仅从「没有前驱 x-1」的数字开始向后计数，避免重复扫描。

【备注】
ACM-lc 目录中已有本题题解，可作为对拍参考。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
