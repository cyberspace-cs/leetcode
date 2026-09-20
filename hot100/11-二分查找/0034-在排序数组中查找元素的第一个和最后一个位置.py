# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 065 / 100 题
================================================================
题号 : 34
标题 : 在排序数组中查找元素的第一个和最后一个位置
难度 : 中等
分类 : 二分查找
链接 : https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
================================================================

【题目描述】
返回目标值在升序数组中的起始与结束下标；不存在则返回 [-1,-1]。

【示例】
nums = [5,7,7,8,8,10], target = 8  →  [3,4]

【思路提示】
两次二分：一次求左边界（找第一个 >= target），一次求右边界（找最后一个 <= target）。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
