# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 100 / 100 题
================================================================
题号 : 287
标题 : 寻找重复数
难度 : 中等
分类 : 技巧
链接 : https://leetcode.cn/problems/find-the-duplicate-number/
================================================================

【题目描述】
长度为 n+1 的数组中数字都在 1..n 之间，只有一个数字重复，找出它；要求不修改数组且使用 O(1) 额外空间。

【示例】
nums = [1,3,4,2,2]  →  2

【思路提示】
把下标映射视为链表指针，用 Floyd 判圈法找环入口即为重复数；也可用二分 + 计数。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
