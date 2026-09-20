# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 099 / 100 题
================================================================
题号 : 169
标题 : 多数元素
难度 : 简单
分类 : 技巧
链接 : https://leetcode.cn/problems/majority-element/
================================================================

【题目描述】
找出数组中出现次数大于 ⌊n/2⌋ 的元素，可以假设该元素一定存在。

【示例】
nums = [2,2,1,1,1,2,2]  →  2

【思路提示】
Boyer-Moore 投票算法：候选数相同时计数 +1，不同则 -1，计数归零时换候选。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
