# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 096 / 100 题
================================================================
题号 : 31
标题 : 下一个排列
难度 : 中等
分类 : 技巧
链接 : https://leetcode.cn/problems/next-permutation/
================================================================

【题目描述】
把数组原地变换为字典序中的下一个更大排列；若不存在更大排列，则变换为升序的最小排列。

【示例】
nums = [1,2,3]  →  [1,3,2]

【思路提示】
从右向左找第一个升序对 (i, i+1)，在右侧找比 nums[i] 大的最小数与它交换，再反转 i 之后的后缀。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
