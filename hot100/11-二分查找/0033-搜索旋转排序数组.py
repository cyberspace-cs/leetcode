# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 064 / 100 题
================================================================
题号 : 33
标题 : 搜索旋转排序数组
难度 : 中等
分类 : 二分查找
链接 : https://leetcode.cn/problems/search-in-rotated-sorted-array/
================================================================

【题目描述】
在某个位置旋转过的升序数组中查找目标值，返回下标，不存在返回 -1。

【示例】
nums = [4,5,6,7,0,1,2], target = 0  →  4

【思路提示】
二分时先判断 [left, mid] 与 [mid, right] 哪一段是有序的，再决定收缩方向。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
