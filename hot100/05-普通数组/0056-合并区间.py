# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 015 / 100 题
================================================================
题号 : 56
标题 : 合并区间
难度 : 中等
分类 : 普通数组
链接 : https://leetcode.cn/problems/merge-intervals/
================================================================

【题目描述】
合并所有重叠的区间，返回互不重叠的区间数组。

【示例】
intervals = [[1,3],[2,6],[8,10],[15,18]]  →  [[1,6],[8,10],[15,18]]

【思路提示】
按左端点排序后一次遍历，判断当前区间是否与结果末尾重叠。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
