# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 073 / 100 题
================================================================
题号 : 739
标题 : 每日温度
难度 : 中等
分类 : 栈
链接 : https://leetcode.cn/problems/daily-temperatures/
================================================================

【题目描述】
给定每日温度，返回每天需要等待多少天才会出现更高的温度；不会出现则记为 0。

【示例】
temperatures = [73,74,75,71,69,72,76,73]  →  [1,1,4,2,1,1,0,0]

【思路提示】
单调递减栈存下标，遇到更高温度时不断弹栈并结算答案。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
