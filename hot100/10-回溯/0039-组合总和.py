# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 057 / 100 题
================================================================
题号 : 39
标题 : 组合总和
难度 : 中等
分类 : 回溯
链接 : https://leetcode.cn/problems/combination-sum/
================================================================

【题目描述】
给定无重复元素的候选数组和目标值，找出所有和为目标的组合，每个数字可被重复选取。

【示例】
candidates = [2,3,6,7], target = 7  →  [[2,2,3],[7]]

【思路提示】
排序 + 回溯，用 start 下标保证组合不重复，剩余值小于当前数时剪枝。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
