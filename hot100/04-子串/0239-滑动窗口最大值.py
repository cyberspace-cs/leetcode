# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 011 / 100 题
================================================================
题号 : 239
标题 : 滑动窗口最大值
难度 : 困难
分类 : 子串
链接 : https://leetcode.cn/problems/sliding-window-maximum/
================================================================

【题目描述】
给定数组和窗口大小 k，窗口每次向右滑动一位，返回每个窗口中的最大值。

【示例】
nums = [1,3,-1,-3,5,3,6,7], k = 3  →  [3,3,5,5,6,7]

【思路提示】
单调递减的双端队列存下标，保证队首始终是当前窗口最大值。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
