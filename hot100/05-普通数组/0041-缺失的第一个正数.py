# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 013 / 100 题
================================================================
题号 : 41
标题 : 缺失的第一个正数
难度 : 困难
分类 : 普通数组
链接 : https://leetcode.cn/problems/first-missing-positive/
================================================================

【题目描述】
找出未在数组中出现的最小正整数，要求 O(n) 时间、O(1) 额外空间。

【示例】
nums = [3,4,-1,1]  →  2

【思路提示】
原地哈希：把数值 x 交换到下标 x-1 处，再找第一个 nums[i] != i+1 的位置。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
