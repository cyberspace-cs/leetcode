# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 098 / 100 题
================================================================
题号 : 136
标题 : 只出现一次的数字
难度 : 简单
分类 : 技巧
链接 : https://leetcode.cn/problems/single-number/
================================================================

【题目描述】
数组中除某个元素只出现一次外，其余元素都出现两次，找出这个只出现一次的元素；要求线性时间、常数空间。

【示例】
nums = [4,1,2,1,2]  →  4

【思路提示】
利用异或性质：x ^ x = 0、x ^ 0 = x，全部异或后结果即为答案。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
