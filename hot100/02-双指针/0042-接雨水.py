# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 006 / 100 题
================================================================
题号 : 42
标题 : 接雨水
难度 : 困难
分类 : 双指针
链接 : https://leetcode.cn/problems/trapping-rain-water/
================================================================

【题目描述】
给定柱子高度数组，计算下雨之后这些柱子之间能接住多少雨水。

【示例】
height = [0,1,0,2,1,0,1,3,2,1,2,1]  →  6

【思路提示】
每格存水量 = min(左侧最高, 右侧最高) - 当前高度；可用双指针或单调栈实现。

【备注】
ACM-lc 目录中已有本题题解，可作为对拍参考。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class Solution:
    def trap(self, height: List[int]) -> int:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
