# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 063 / 100 题
================================================================
题号 : 4
标题 : 寻找两个正序数组的中位数
难度 : 困难
分类 : 二分查找
链接 : https://leetcode.cn/problems/median-of-two-sorted-arrays/
================================================================

【题目描述】
给定两个正序数组，返回它们合并后的中位数，要求时间复杂度 O(log(m+n))。

【示例】
nums1 = [1,3], nums2 = [2]  →  2.0

【思路提示】
在较短数组上二分划分点，使左半部分元素总数正确且「左最大 ≤ 右最小」。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
