# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 086 / 100 题
================================================================
题号 : 198
标题 : 打家劫舍
难度 : 中等
分类 : 动态规划
链接 : https://leetcode.cn/problems/house-robber/
================================================================

【题目描述】
相邻房屋不能在同一晚被偷，求在不触发报警的前提下能偷到的最大金额。

【示例】
nums = [2,7,9,3,1]  →  12

【思路提示】
dp[i] = max(dp[i-1], dp[i-2] + nums[i])，同样可滚动优化空间。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class Solution:
    def rob(self, nums: List[int]) -> int:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
