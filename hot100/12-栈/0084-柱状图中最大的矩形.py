# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 070 / 100 题
================================================================
题号 : 84
标题 : 柱状图中最大的矩形
难度 : 困难
分类 : 栈
链接 : https://leetcode.cn/problems/largest-rectangle-in-histogram/
================================================================

【题目描述】
给定柱状图中各柱子的高度，求其中能勾勒出的最大矩形面积。

【示例】
heights = [2,1,5,6,2,3]  →  10

【思路提示】
单调递增栈（首尾各补一个 0），弹栈时以该柱高为矩形高计算面积。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
